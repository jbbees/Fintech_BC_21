# Yen Futures: Should we buy JPY?

<details><summary>Premise:</summary>

* We need to decide if it is financially sound to buy Japanese Yen (JPY) now based on predicted future returns and volatilty.
* We need to forecast the next **5 days** of Yen volatilty and returns, predict if returns are increasing/decreasing that favors buying.
* We will use historic-time series data on Yen returns, and build a series of different models based on different methods *ARMA*, *ARIMA*, *GARCH* using **statsmodels** module.
* We will also use **sklearn** module to make Linear Regression models, splitting the yen data into training and test components, and Rolling Out-of-Sample methods to test the models goodness of fit with the model.
</details>

<details><summary>Installs needed</summary>

Most of time-series model functions are built-in. To import these modules:

`from statsmodels.tsa.arima_model import ARMA` and `import ARIMA`

For the 

For the GARCH model:
`conda install -c bashtage arch` or you simply use `pip install arch`

`from arch import arch_model`
</details>

<details><summary>What does the yen data file contain?</summary>

Run a simple `.shape` or  on the raw dataframe and it will

* Date, which is the index column because we need to be able to depreciate parts of the date. 
* Open, opening price for the Yen that day.
* High, the highest price for the yen in that day.
* Low, the lowest price for the Yen in the day.
* Last
* Settle
* Volume, the amount of yen traded that day.
* Previous Day Open Interest
</details>

# Part 1: Time-Series Analysis

## Imports:
<pre><code>
import numpy as np
import pandas as pd
from pathlib import Path
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
</code></pre>

You'll need to import the `sickit-learn` modules. I did this at the

<pre><code>
import statsmodels.api as sm
</code></pre>

## Read-in data and cleanup
<pre><code>
yen_futures = pd.read_csv(
    Path("yen.csv"), index_col="Date", infer_datetime_format=True, parse_dates=True
)
yen_futures.head()
</code></pre>
<details><summary>What you should see</summary></details> 

Slice the dataframe. Only use rows from **Jan 1 1990 to present**. 
<pre><code>yen_futures = yen_futures.loc["1990-01-01":, :]</code></pre>

Plot the raw returns based on the *Settle* column of the dataset.
<pre><code>yen_futures['Settle'].plot(title='Yen Futures Settle Prices', ylabel='Settle Price in $USD', figsize=(15,10))</code></pre>

<details><summary>Interpretation of data</summary>
Overall the view of the data looks non-stationary and that some kind of trend exists. I am seeing a pattern of gradual incrases followed by gradual decreases, in approximately 4-year intervals. From 1992-1996 there's increase from 6000-12,700, and the from 1996-2000 it gradually declines below 7000 by 1998-1999. There's intermittent bursts of micro-increases and decreases in the trends, likely seasonality is playing a role in that. Year-over-year along the x-axis, we see from approx years 2003-2013 there's a trending increase the spikes in data getting more pronounced. Lots of spikiness plotted raw data presented.</details>



