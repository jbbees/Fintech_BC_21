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

1. Read in the Yen daily data. This is the same as Part 1.

<pre><code>
yen_futures = pd.read_csv(
    Path("yen.csv"), index_col="Date", infer_datetime_format=True, parse_dates=True
)
</code></pre>

2. Slice the data for only rows in the year 1990.
<pre><code>yen_futures = yen_futures.loc["1990-01-01":, :]</code></pre>

3. Decompose the *Settle* column to be in stationary format.

<pre><code>
settle_returns = yen_futures['Settle'].pct_change() * 100
settle_returns.dropna(inplace=True)
settle_returns.plot()
</code></pre>
