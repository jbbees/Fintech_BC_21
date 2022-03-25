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

4. Add a column called *Lagged Returns* 
<pre><code>
yen_futures['Return'] = settle_returns.copy()
yen_futures['Lagged_Return'] = settle_returns.shift()
yen_futures.dropna(inplace=True)
yen_futures.head()
</code></pre>

After running `yen_futures.shape` there should now be 1,415 rows and 10 columns. This is much lower than the 7.515 rows from Part 1. 

# Separate the training (in-sample) independent features and y dependent components

1. Create a train/test split

<pre><code>train = yen_futures[:'2017']
test = yen_futures['2018':]
</code></pre>


