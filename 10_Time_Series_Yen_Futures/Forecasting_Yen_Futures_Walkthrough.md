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

> import numpy as np
> import pandas as pd
> from pathlib import Path
> %matplotlib inline
> import warnings
> warnings.filterwarnings('ignore')

## Read-in data and cleanup








