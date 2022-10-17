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
#### Visual 7 - Parallel Coordinates Plot
#### Visual 8 - Parallel Categories Plot
#### Visual 9 - Plotly Sunburst Chart
## Panel Pane Markdown Notes
These are just contextual Markdown notes that will be displayed along with the visual in each tab. Such as, a general welcome note, or other analysis notes. Each message is within a `panel.pane.Markdown()` function. I won't list them all here. But every message is presented this way. 

Standard Welcome message
```
welcome = pn.pane.Markdown(
    """
This dashboard presents a visual analysis of historical prices of house units,
sale price per square foot and gross rent in San Francisco, California
from 2010 to 2016.
You can navigate through the tabs above to explore
more details about the evolution of the real estate market on
The Golden City across these years.
"""    
)
```
## Main Program
The core code. This program defines 9 custom functions for each visual. When the dashboard is executed, each visual function is executed, builds the visual, and returns it to the dashboard. 

```
def housing_units_per_year():                              # for some reason we are not passing anything into these visual functions. 
    """Housing Units Per Year."""
    
    # YOUR CODE HERE!
    housing_units = pd.DataFrame(
        sfo_data,
        columns=['year', 'housing_units']
    ).groupby('year')['housing_units'].mean().reset_index()

    # Make a visual plot
    housing_plot = housing_units.hvplot.bar(
    x='year',
    y='housing_units',
    width=1200,
    color='yellow',
    alpha=.2
    ).opts(xformatter='%.0f', title='SFO Housing Units Sold 2010-2016', invert_axes=True)
    housing_plot
    return housing_plot
    
def average_gross_rent():
    """Average Gross Rent in San Francisco Per Year."""
    
    # YOUR CODE HERE!
    rent = pd.DataFrame(
        sfo_data,
        columns=['year', 'gross_rent']
    ).groupby('year')['gross_rent'].mean().reset_index()
    
    rent_plot = rent.hvplot.bar(
    x='year',
    y='gross_rent',
    width=1200,
    color='purple',
    alpha=.2                               
    ).opts(xformatter='%.0f', title='SFO Gross Rent Sold 2010-2016', invert_axes=True)
    return rent_plot
    
def average_sales_price():
    """Average Sales Price Per Year."""
    
    # YOUR CODE HERE!
    sales_price = pd.DataFrame(
        sfo_data,
        columns=['year', 'sale_price_sqr_foot']
    ).groupby('year')['sale_price_sqr_foot'].mean().reset_index() 
    return sales_price
    
def average_price_by_neighborhood():
    """Average Prices by Neighborhood."""
    
    # YOUR CODE HERE!

    sfo_neighborhood_data = sfo_data.groupby(['year', 'neighborhood'])['sale_price_sqr_foot'].mean().reset_index()

    neighborhood_plot = sfo_neighborhood_data.hvplot.line(
        "year",
        "sale_price_sqr_foot",
        xlabel="Year",
        ylabel="Avg. Sale Price per Square Foot",
        groupby="neighborhood",                                            # this will create an interactive dropdown per neighborhood
    )
    return neighborhood_plot

def top_most_expensive_neighborhoods():
    """Top 10 Most Expensive Neighborhoods."""

    # YOUR CODE HERE!
    expensive = sfo_data.groupby('neighborhood')['sale_price_sqr_foot'].mean().reset_index()
    expensive.sort_values('sale_price_sqr_foot', ascending=False, inplace=True)
    top_10 = expensive.nlargest(10, 'sale_price_sqr_foot')
    return top_10
    
def most_expensive_neighborhoods_rent_sales():
    """Comparison of Rent and Sales Prices of Most Expensive Neighborhoods."""   
    
    # YOUR CODE HERE!
    sfo_neighborhood_data = sfo_data.groupby(['year', 'neighborhood']).mean().reset_index()       # this will keep all columns.      

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
    return sfo_compare_plot

```

## Build the Dashboard
This dashboard will be 5 tabs. Each tab has a name, and will call a function(s) in the main program to be assembled and returned/displayed in that tab. And we will present the content of each tab in either a `panel.Row` or `panel.Column`

Create the tabs
```
tabs = pn.Tabs(
    ('Welcome', pn.Row(welcome, neighborhood_map())),                                                # this is the first pane the user will see. 
    ('Yearly Market Analysis', pn.Column(market_note, average_gross_rent(), average_sales_price())),
    ('Neighborhood Analysis', pn.Column()),
    ('Parallel Plots Analysis', pn.Column(parallel_coordinates(), parallel_categories())),
    ('Sunburst', pn.Column(sunburst()))
)
```
Run the dashboard. Pass the tabs into it. 
```
sfo_dashboard = pn.Column(
    pn.Row(title),                      # title on top
    tabs,                               # pass in our 5 tabs that each have their own visuals.
    width=900 
)
```


## Serve the Dashboard 
```
pn.extension('bokeh')                              # enable the bokeh extension
sfo_dashboard.servable()                           # serve the dashbaord to the bokeh server
```
