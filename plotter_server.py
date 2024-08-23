# import pprint
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Dict
import uvicorn
# import json

app = FastAPI()

# TODO - make it so that we can spawn new window with separate metrics and title so that we can mode it around
# TODO start on first data, stop showing when data not received in x time
# TODO have plot despawn on timer if no data received in X time (TTL should be configurable when spawning new plot)
# TODO make it into a proper repo and put ip up on github

# Initial Configuration
CONFIG = {
    'plot_title': 'A graph',
    'x_label': 'Time',
    'y_label': 'Value',
    # 'x_range': (0, 100),
    'y_range': (0, 200),
    'data_sets': {
        'set1': {'color': 'r', 'label': 'Target security', 'marker': 'o'},
        'set2': {'color': 'b', 'label': 'Target money', 'marker': 's'},
        'set3': {'color': 'g', 'label': 'Overall money', 'marker': ','},
    },
    'legend_location': 'upper left',
    'max_points': 180,
}

all_plots = {
    # 1:{},2:{}
    # 1:{
    #     # 'data_sets':  {
    #     #     },
    #     # 'fig': None,
    #     # 'ax': None,
    #     # 'lines': {},
        
    #     # 'max_points': 180,
    #     # 'legend_location': 'upper left',
    # },
}

for x in range(2):
    all_plots[x] = {}
    ap = all_plots[x]
    ap['fig'], ap['ax'] = plt.subplots()
    ap['data_sets'] = {}
    ap['lines'] = {}
    ap['legend_location'] = CONFIG['legend_location']
    ap['max_points'] = CONFIG['max_points']

# all_plots[2]['fig'], all_plots[2]['ax'] = plt.subplots()
# all_plots[1]['data_sets'] = {}

def update_plot_config(plot_id, data):
    global all_plots
    ap = all_plots[plot_id]
    try:
        ap['max_points'] = int(data.max_points)
    except:
        ap['max_points'] = CONFIG['max_points']
    try:
        ap['legend_location'] = data.legend_location
    except:
        ap['legend_location'] = CONFIG['legend_location']

    ax = ap['ax']
    ax.clear()
    ax.set_title(data.plot_title ) # mandatory
    ax.set_xlabel(data.x_label)
    ax.set_ylabel(data.y_label)
    # ax.set_xlim(CONFIG['x_range']) # this is set dynamically
    ax.set_ylim((data.y_range[0],data.y_range[1])) # add try except here
    # ax.set_ylim(CONFIG['y_range'])
    # mandatory, no defaults
    ap['lines'] = {}
    for k,v in data.data_sets.items():
        ap['lines'][k] = ax.plot([], [], color=v.color, marker= v.marker, label=v.label)[0]
        anot = ax.annotate(k, xy=(0, 0), xytext=(5, 0), textcoords='offset points', ha='left', va='center', color=v.color) 
        ap['data_sets'][k] = {'x': [], 'y': [], 'anot': anot}
    ax.legend(loc=ap['legend_location'], prop={'size': 6})
    ax.grid(axis='x')

class DataPoint(BaseModel):
    x: float
    y: float

class DataPointList(BaseModel):
    datapoints: list[DataPoint]

# class DataMultiset(BaseModel):
#     multiset: Dict[str, DataPoint]

class DataMegaset(BaseModel):
    megaset: Dict[str, DataPointList]

@app.post("/id/{plot_id}/megaset") 
async def receive_multiset_data(plot_id: int, data: DataMegaset):
    if plot_id not in all_plots.keys():
        return {"status": "Attempting to send data to nonexistant plot, spawn it first via /config endpoint!"}
    data_sets = all_plots[plot_id]['data_sets']
    for k,v in data.megaset.items():
        # print(f'DBG megaset k: {k} v{v}')
        dsn = data_sets[k]
        for dp in v.datapoints:
            dsn['x'].append(dp.x)
            dsn['y'].append(dp.y)
        while len(dsn['x']) > all_plots[plot_id]['max_points']:
            dsn['x'].pop(0)
            dsn['y'].pop(0)
    # if set_name not in all_plots[plot_id]['data_sets']:
    #     return {"status": "Invalid set name!"}
    print(f"Received data point megaset for id={plot_id} ") # maybe more debug here
    return {"status": "Megaset received"}


@app.post("/id/{plot_id}/set/{set_name}") # U/CRUD
async def receive_data(plot_id: int, set_name: str, data: DataPoint):
    if plot_id not in all_plots.keys():
        return {"status": "Attempting to send data to nonexistant plot, spawn it first via /config endpoint!"}
    if set_name not in all_plots[plot_id]['data_sets']:
        return {"status": "Invalid set name!"}

    data_sets = all_plots[plot_id]['data_sets']
    dsn = data_sets[set_name]
    dsn['x'].append(data.x)
    dsn['y'].append(data.y)
    
    while len(dsn['x']) > all_plots[plot_id]['max_points']:
        dsn['x'].pop(0)
        dsn['y'].pop(0)
    
    print(f"Received data point for id={plot_id} set={set_name}: x={data.x}, y={data.y}")
    return {"status": "Data received"}

class DataSet(BaseModel):
    color: str
    label: str
    marker: str

class DataFrame(BaseModel):
    plot_title: str
    x_label: str
    y_label: str
    data_sets: Dict[str, DataSet] = Field(..., min_items=1)
    y_range: list
    max_points: int

    class Config:
        extra = "allow" 

@app.post("/config/{plot_id}") # CU/CRUD
async def update_config(plot_id: int, data: DataFrame):
    update_plot_config(plot_id, data)
    return {"status":"Config received and updated", "plot_id": plot_id, "plot_title": data.plot_title}
    
def update_plot(frame): # tried to have it parametrizable but no bueno :/
    # dynamic X range (in time), do it separately for each plot based on it's datasets
    ret = []
    global all_plots

    for plot in all_plots.values():    
        data_sets = plot['data_sets']
        pax = plot['ax']

        all_x = [x for set_data in data_sets.values() for x in set_data['x']]
        if all_x:
            x_min, x_max = min(all_x), max(all_x)
            pax.set_xlim(x_min, x_max)

        for set_name, line in plot['lines'].items():
            line.set_data(data_sets[set_name]['x'], data_sets[set_name]['y'])
            ret.append(line)
        # experimental - dynamically changing legend based on whats in view
        pax.relim()
        pax.autoscale_view(scalex=True, scaley=True)  # Only autoscale y-axis
        visible_lines = []
        visible_labels = []
        for line in pax.get_lines():
            if line.get_visible():
                xdata = line.get_xdata()
                ydata = line.get_ydata()
                if len(xdata) > 0:
                    xmin, xmax = pax.get_xlim()
                    ymin, ymax = pax.get_ylim()
                    if (xmin <= xdata[-1] <= xmax) and (ymin <= ydata[-1] <= ymax):
                        visible_lines.append(line)
                        visible_labels.append(line.get_label())
        pax.legend(visible_lines, visible_labels, loc=plot['legend_location'], prop={'size': 6})
    return ret

# return must be a tuple or list of ax.plot and similar ax. objects


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

def run_plot():
    anims = []
    for plot_v in all_plots.values():
        anims.append(FuncAnimation(plot_v['fig'], update_plot, interval=100, blit=False))
    plt.show()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    run_plot()