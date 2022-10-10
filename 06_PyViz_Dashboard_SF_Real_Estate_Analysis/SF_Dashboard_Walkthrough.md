# Real Estate Analysis Dashboard

We're taking historical real estate data for San Francisco, running price analysis, and make an interactive visualiztion notebook using PyViz visual libraries and Mapbox API mapping charts to show housing prices in geographic areas. We will then assemble these charts into a central user dashboard and publish to online bokeh server.

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

## Part 1: San Franscisco Rental Analysis
