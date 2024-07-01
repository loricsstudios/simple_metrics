import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fastapi import FastAPI
# , HTTPException, Request
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
    'plot_title': 'Graph x',
    'x_label': 'Time',
    'y_label': 'Values',
    # 'x_range': (0, 100),
    'y_range': (0, 100),
    'data_sets': {
        'set1': {'color': 'r', 'label': 'Target security', 'marker': 'o'},
        'set2': {'color': 'b', 'label': 'Target money', 'marker': 's'},
        'set3': {'color': 'g', 'label': 'Overall money', 'marker': '^'},
    },
    'legend_location': 'upper right',
    'max_points': 180,
}







all_plots = {
    '1':{
        'data_sets':  {set_name: {'x': [], 'y': []} for set_name in CONFIG['data_sets']},
        'fig': None,
        'ax': None,
        'lines': {},
        'TTL': None, 
    },
    '2':{
        'data_sets':  {set_name: {'x': [], 'y': []} for set_name in CONFIG['data_sets']},
        'fig': None,
        'ax': None,
        'lines': {},
        'TTL': None, 
    }
} #TBD

all_plots['1']['fig'], all_plots['1']['ax'] = plt.subplots()
all_plots['2']['fig'], all_plots['2']['ax'] = plt.subplots()

def update_plot_config(plot_id):
    ax = all_plots[plot_id]['ax']
    ax.clear()
    ax.set_title(CONFIG['plot_title'])
    ax.set_xlabel(CONFIG['x_label'])
    ax.set_ylabel(CONFIG['y_label'])
    # ax.set_xlim(CONFIG['x_range'])
    ax.set_ylim(CONFIG['y_range'])
  
    all_plots[plot_id]['lines'] = {set_name: ax.plot([], [], 
                               f"{CONFIG['data_sets'][set_name]['color']}{CONFIG['data_sets'][set_name]['marker']}-", 
                               label=CONFIG['data_sets'][set_name]['label'])[0] 
             for set_name in CONFIG['data_sets']}

    ax.legend(loc=CONFIG['legend_location'])

CONFIG['plot_title'] = "apples"
update_plot_config('1')
CONFIG['plot_title'] = "bananas"
update_plot_config('2')

class DataPoint(BaseModel):
    # id: str
    x: float
    y: float



@app.post("/id/{plot_id}/set/{set_name}") # U/CRUD
async def receive_data(plot_id: str, set_name: str, data: DataPoint):
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

@app.post("/config") # CU/CRUD
async def update_config(data: DataFrame):
    return {"status":"Config received", "plot_title": data.plot_title}
    # try:
    #     parsed_data = json.loads(data)
    #     for key, value in parsed_data.items():
    #         if key in CONFIG:
    #             CONFIG[key] = value
    #     update_plot_config()
    #     return {"status": "Configuration updated", "config": CONFIG}
    # except json.JSONDecodeError:
    #     return {"status": "Error", "message": "Invalid JSON"}
    

def update_plot(frame): # tried to have it parametrizable but no bueno :/
    # dynamic X range (in time), do it separately for each plot based on it's datasets
    ret = []

    for plot in all_plots.values():    
        # plot = all_plots['1'] # try redo this as a method of object so it can still be callable without param?
        data_sets = plot['data_sets']

        all_x = [x for set_data in data_sets.values() for x in set_data['x']]
        if all_x:
            x_min, x_max = min(all_x), max(all_x)
            plot['ax'].set_xlim(x_min, x_max)

        for set_name, line in plot['lines'].items():
            line.set_data(data_sets[set_name]['x'], data_sets[set_name]['y'])
            ret.append(line)
        
        plot['ax'].relim()
        plot['ax'].autoscale_view(scalex=False, scaley=True)  # Only autoscale y-axis
    return ret
# return must be a tuple or list of ax.plot objects
#tuple(plot['lines'].values())

def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

def run_plot():
    anims = []
    for plot_k, plot_v in all_plots.items():
        anims.append(FuncAnimation(plot_v['fig'], update_plot, interval=100, blit=False))
    
    # anims = (FuncAnimation(plot_v['fig'], update_plot, interval=100, blit=True))
    print(f'num of anims: {len(anims)}')
    plt.show()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    run_plot()