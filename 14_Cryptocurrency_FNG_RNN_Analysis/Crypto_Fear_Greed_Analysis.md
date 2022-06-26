# Bitcoin Fear & Greed Index, LSTM RNN Price Predictor

This program is building a recurrent neural network (RNN) to predict future Bitcoin prices based on a combination of past prices and crypto sentiment. We're using time-series BTC price data from the Fear & Greed (FNG) Index of crypto sentiment scores and closing prices. We will be building a deep RNN model utilizing long short-term memory (LSTM) architecture within the keras tensorflow feature set, to predict the future closing price of BTC using the past rolling-window of 10 days worth of crypto pricing and the sentiment scores of crypto reported that day. 

## The Data

We are provided with files of BTC closing prices as well as FNG sentiment scoring for Bitcoin on that unique trading day. We didn't need to fetch the data for this particular excercise, and there's no need to do sentiment analysis since it was done by the FNG, so it can be read-in. But the setup for our RNN model is predicting on a rolling-window

* The FNG sentiment scores come from various crypto news sources the Index web scrapes for that trading day in BTC.
* The closing price is whatever the BTC was. Except there is no real closing time period in crypto. Crypto is traded world-wide 24/7, so we will assume this is going up to 11:59PM each day. 
* Splitting the data 70/30. 70% of the BTC price data will be exposed to the model.
* Rolling windw of 10-days.
* The RNN model will be a deep, 3-layered model with LSTM layers feeding input data into the next layer.


## Imports
```
import numpy as np
import pandas as pd
import hvplot.pandas

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

from numpy.random import seed
seed(1)
from tensorflow import random
random.set_seed(2)
```

## Data Pre-Processing

This will be kind of a complicated way of separating the X & y components. We are not just setting the target to a column, and the X features to everything else. The dataframe itself is very basic. This time we're building a custom **function** that will use a for-loop to iterate through the BTC data, and append the *column numbers* of X and y components to their own lists.  

We will define a function using the `window_data()` function. Pass in the following 4 arguments: *the raw DataFrame of BTC prices and sentiment scores*, *window of 10 days*, *the column number of the feature column*, and *the column of the Bitcoin closing price*.

We weill append the X predictive features to the empty list **X** and closing price y-targets to the list called **y**

```
def window_data(df, window, feature_col_number, target_col_number):
    X = []
    y = []
    for i in range(len(df) - window - 1):
        features = df.iloc[i:(i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)
```

Define the 4 needed arguments. `window_size` is 10 for 10-day rolling window of prices. X column is the 0th column and the target closing price is the 1 column. Call on this window_data function. 
```
window_size = 10
feature_column = 0
target_column = 1
X, y = window_data(df, window_size, feature_column, target_column)
```


