# Part 2: Linear Regression Analysis

We are going to see if a Linear Regression analysis will fair better than the ARMA, ARIMA models. 

# Imports

<pre><code>import numpy as np
import pandas as pd
from pathlib import Path
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')
</code></pre>

# Read-in data and cleanup

This is the same as Part 1.

<pre><code>
yen_futures = pd.read_csv(
    Path("yen.csv"), index_col="Date", infer_datetime_format=True, parse_dates=True
)
</code></pre>
