# import pprint
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Dict
import uvicorn

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
    'y_range': (0, 100),
    'data_sets': {
        'set1': {'color': 'r', 'label': 'Target security', 'marker': 'o'},
        'set2': {'color': 'b', 'label': 'Target money', 'marker': 's'},
        'set3': {'color': 'g', 'label': 'Overall money', 'marker': ','},
    },
    'legend_location': 'upper right',
    'max_points': 180,
}

all_plots = {
    1:{
        'data_sets':  {
                # 'empty': {'x': [], 'y': [], 'anot': None} 
            },
        'fig': None,
        'ax': None,
        'lines': {},
        'TTL': None, 
    },
    # '2':{
    #     'data_sets':  {set_name: {'x': [], 'y': []} for set_name in CONFIG['data_sets']},
    #     'fig': None,
    #     'ax': None,
    #     'lines': {},
    #     'TTL': None, 
    # }
}

all_plots[1]['fig'], all_plots[1]['ax'] = plt.subplots()
# all_plots['2']['fig'], all_plots['2']['ax'] = plt.subplots()

def update_plot_config(plot_id, data):
    global all_plots
    ax = all_plots[plot_id]['ax']
    ax.clear()
    ax.set_title(data.plot_title ) # mandatory
    ax.set_xlabel(data.x_label)
    ax.set_ylabel(data.y_label)
    # ax.set_xlim(CONFIG['x_range']) # this is set dynamically
    ax.set_ylim(data.y_range)
    # mandatory, no defaults
    all_plots[plot_id]['lines'] = {}
    for k,v in data.data_sets.items():
        all_plots[plot_id]['lines'][k] = ax.plot([], [], color=v.color, marker= v.marker, label=v.label)[0]
        anot = ax.annotate(k, xy=(0, 0), xytext=(5, 0), textcoords='offset points', ha='left', va='center', color=v.color) 
        all_plots[plot_id]['data_sets'][k] = {'x': [], 'y': [], 'anot': anot}
    ax.legend(loc=data.legend_location, prop={'size': 6})

class DataPoint(BaseModel):
    x: float
    y: float


# @app.delete("/id/{plot_id}")
# async def despawn_plot(plot_id: str):
#     return {"status" : f"hello world! plot id to be deleted: {plot_id}"}

@app.post("/id/{plot_id}/set/{set_name}") # U/CRUD
async def receive_data(plot_id: int, set_name: str, data: DataPoint):
    if plot_id not in all_plots.keys():
        return {"status": "Attempting to send data to nonexistant plot, spawn it first via /config endpoint!"}
    if set_name not in all_plots[plot_id]['data_sets']:
        return {"status": "Invalid set name!"}

    data_sets = all_plots[plot_id]['data_sets']
    data_sets[set_name]['x'].append(data.x)
    data_sets[set_name]['y'].append(data.y)
    
    if len(data_sets[set_name]['x']) > CONFIG['max_points']:
        data_sets[set_name]['x'].pop(0)
        data_sets[set_name]['y'].pop(0)
    
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

        all_x = [x for set_data in data_sets.values() for x in set_data['x']]
        if all_x:
            x_min, x_max = min(all_x), max(all_x)
            plot['ax'].set_xlim(x_min, x_max)

        for set_name, line in plot['lines'].items():
            line.set_data(data_sets[set_name]['x'], data_sets[set_name]['y'])
            ret.append(line)
        for v in data_sets.values(): # highly experimental /debug
            # print(v['anot'])
            v['anot'].set_position((v['x'][-1], v['y'][-1]))
            ret.append(v['anot'])

        
        plot['ax'].relim()
        plot['ax'].autoscale_view(scalex=True, scaley=True)  # Only autoscale y-axis
    return ret

    # for i, (x, y) in enumerate(samples): #maybe belongs here? trying to annotate axes
    # plt.plot(x, y)
    # plt.text(x[-1], y[-1], f'sample {i}')
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