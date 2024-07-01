# Simple metrics

*Claude+ Uvicorn + Matplotlib = <3*

This is a simple python webserver that listens on a port to data coming to different endpoints and proceeds to plot the data visually.

## Prerequisites

* Python 3.12+

## Basic usage

* initialize local environment using the included `local_init.sh` or by simply setting up python virtual env and installing the dependencies 
* run `python3 plotter_server.py` - it should start listening on on port 8000 on `http://localhost:8000` for requests coming to various endpoints (see the `plotter_server.py` for details)
* the endpoints mostly expect POST requests with JSON payloads in specific structure (see examples below)



### Spawning new plots

* 

### Feeding data to the plots / plotting the graphs

### Despawning plots



## Credits, links

There would be nothing without the following:

* [Anthropic Claude 3.5]() (doing the heavy lifting)
* [Matplotlib]()
* [Pydantic]()
* [Uvicorn]()

## Why? 

When I started playing *BitRunner* game, one of the painpoints was the difficulty visualizing in real time how my NS scripts are doing. I had the flash of inspiration - hey, this is javascript (in the game) and it must be able to call out using some http requests. It does, so a bit of *Claude* rapid prototyping gave me something to work with and I had a working proof of concept within minutes. 

### BitRunner game specific

* example javascripts to use within BitRunner can be seen in the `bitrunner/` folder
* `plot.js` - simply ingests the JSON.strigify'ed data and POSTs it to a specified endpoint on the `http://localhost:8000`
* `graph.js` - example of how to display simple metrics for a target server (it's accumulated money in % as well as security strength in % over base) in the game alongside your own wealth (logarithmic graph). Those three metrics are useful for gaining insight into how your scripts are performing against a server
* once you have the server running and listening for incoming requests, in the game's Terminal simply `run graph.js someservername 1` should start drawing the metrics

## Author

me, myself and FF:06:B5