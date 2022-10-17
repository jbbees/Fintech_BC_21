# Real Estate Analysis Dashboard - Mapbox API

We're taking real estate data for San Francisco from 2010-2016, running price analysis, and make an **9** interactive visualiztions using PyViz visual libraries and Mapbox API mapping charts to show housing prices in geographic areas. We will then assemble these charts into a central user panel dashboard and publish to an online bokeh server.

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
## Read-in Data Files 

We have 2 simple files. `sfo_neighborhoods_census_data.csv` which is the primary data on rent, and housing sales. And `neighborhoods_coordinates.csv` which geocoded data for mapping charts.

```
sfo_data = pd.read_csv('resources/sfo_neighborhoods_census_data.csv')
sfo_map_data = pd.read_csv('resources/neighborhoods_coordinates.csv')

# Making backup copies
sfo_data1 = sfo_data.copy()
sfo_data2 = sfo_data1.copy()
sfo_data3 = sfo_data2.copy()
```
## Visual Charts

#### Visual 1 - Housing Units Per Year

Visual of how many housing units were sold on average per year from 2010-2016.

```
housing_units = pd.DataFrame(
        sfo_data,
        columns=['year', 'housing_units']
    ).groupby('year')['housing_units'].mean().reset_index()

```
Plot 

```
housing_plot = housing_units.hvplot.bar(
    x='year',
    y='housing_units',
    width=1200,
    color='yellow',
    height=300,
    alpha=.2                               # make the graph color more transparent
).opts(yformatter='%.0f', title='SFO Housing Units Sold 2010-2016', invert_axes=False)
housing_plot
```



#### Visual 2 - Rent per year 

Visual of average rent expense from 2010-2016. Slice the data for just year and rent columns. Group by the year and average the rent value.

```
rent = pd.DataFrame(
        sfo_data,
        columns=['year', 'gross_rent']
    ).groupby('year')['gross_rent'].mean().reset_index()
```

Plot

```
rent_plot = rent.hvplot.bar(
    x='year',
    y='gross_rent',
    width=1200,
    color='purple',
    alpha=.2                               
).opts(xformatter='%.0f', title='SFO Gross Rent Sold 2010-2016', invert_axes=True)
rent_plot
```


#### Visual 3 - Sale price

Visual of average sales prices from 2010-2016. This will be a dropdown selector where each unique neighborhood can be selected and it'll display an hvplot line graph. 

```
sfo_neighborhood_data = sfo_data.groupby(['year', 'neighborhood'])['sale_price_sqr_foot'].mean().reset_index()
```

```
neighborhood_plot = sfo_neighborhood_data.hvplot.line(
        "year",
        "sale_price_sqr_foot",
        xlabel="Year",
        ylabel="Avg. Sale Price per Square Foot",
        groupby="neighborhood",
    )
neighborhood_plot
```

#### Visual 4 - Top 10 Expensive Neighborhoods (Sales Price)

Visual of the top 10 most expensive neighborhoods based on home sales price. I first groupby the neighborhood. Then run the average on sales price per neighborhood. I slice the data again using the `nlargest()` function. 

```
expensive = sfo_data.groupby('neighborhood')['sale_price_sqr_foot'].mean().reset_index()        
expensive.sort_values('sale_price_sqr_foot', ascending=False, inplace=True)
top_10= expensive.nlargest(10, 'sale_price_sqr_foot')
```
```
top_10_plot = top_10.hvplot.bar(
    x='neighborhood',
    y='sale_price_sqr_foot',
    color='green',
    alpha=.2,
    width=1000,
    rot=45,
).opts(xformatter='%.0f', title='SFO Top 10 Expensive Neighborhoods (Sale Price per Sq Ft)', invert_axes=True)
top_10_plot
```

#### Visual 5 - Comparison of Rent vs Sales Prices

Comparison visual of average rent vs average sales prices per year, per neighborhood. This will be a dropdown selector for neighborhood which displays duo-bar charts of rent compared to sales price.

```
sfo_neighborhood_data = sfo_data.groupby(['year', 'neighborhood']).mean().reset_index()
```

```
sfo_compare_plot = sfo_neighborhood_data.hvplot.bar(
    'year',
    ['sale_price_sqr_foot', 'gross_rent'],      # this list will generate 2 bars per each column, per each year
    xlabel='Year',
    ylabel='Number of Housing Units',
    groupby='neighborhood',                     # initialize a drowdown selector per neighborhood 
    height=700,
    width=1000,
    rot=90
)
sfo_compare_plot
```

#### Visual 6 - Mapbox Plot

Visual that constructs the map using the Mapbox API. This requires concatenating the 2 data files togehter. We need the latitude and longitude colimns.
```
df1 = sfo_data
df2 = sfo_map_data                                                  # geocoded data
sfo_combined = pd.concat([df1, df2], axis=1, join='inner')

```
Initialize the mapbox access token
```
px.set_mapbox_access_token(map_box_api)
```
Build the map.
```
sfo_neighborhood_map = px.scatter_mapbox(
    sfo_combined,
    lat='Lat',                                                       # latitude
    lon='Lon',                                                       # longitude
    size='sale_price_sqr_foot',                                      # sales price is the bubble size. The larger the bubble correlates to larger rent. 
    color='gross_rent',                                              # rent is the category.
    size_max=15,
    zoom=11,
    color_continuous_scale=px.colors.cyclical.IceFire,
    hover_name='Neighborhood',                                       # this will show the neighborhood name when you hover a mouse over a data-bubble. 
    title='SFO Average Rent per Neighborhood'
)
sfo_neighborhood_map.show()
```
## Visual 7
## Visual 8
## Visual 9 - Plotly Sunburst Chart
## Analysis Markdown Notes


## Main Program
## Build the Dashboard
## Serve the Dashboard 
