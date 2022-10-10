# Real Estate Analysis Dashboard - Mapbox API

We're taking real estate data for San Francisco, running price analysis, and make an interactive visualiztion notebook using PyViz visual libraries and Mapbox API mapping charts to show housing prices in geographic areas. We will then assemble these charts into a central user panel dashboard and publish to online bokeh server.

## Imports

```
import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')
```
## Mapbox API setup

We need to embed the Mapbox API using the plotly-express library. Note: there are issues with the API keys not rendering as **str** types. 

```
load_dotenv()                                    
map_box_api = os.getenv("mapboxapi")
```
Check to make sure the API keys are **str** If not, manually assign the public key. (Not recommended, but maobox is not embedding corectly)
```
if map_box_api is None:                        # if it's NoneType
    print('*' * 50)
    print(f'The API keys failed to load correctly. Data-type is, {type(map_box_api)}')
    map_box_api = 'pk.eyJ1IjoiamJiZWVzIiwiYSI6ImNrbWVwOTEyMDAxMjQycGsxcG9tNHc2MHAifQ.ZghsiGuJ06OzYBAsQw43Nw'        # this is my public key. 
else:
    print(f'Success, {type(map_box_api)}')     # should be a string
```
Set the mapbox access token
```
px.set_mapbox_access_token(map_box_api)
```


## Part 1: San Franscisco Rental Analysis
