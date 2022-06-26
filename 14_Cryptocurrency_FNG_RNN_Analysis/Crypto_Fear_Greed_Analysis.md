# Bitcoin Fear & Greed Index, LSTM RNN Price Predictor

We're using time-series BTC price data from the Fear & Greed (FNG) Index of crypto sentiment scores and closing prices. We will be building a deep RNN model utilizing long short-term memory (LSTM) architecture within keras tensorflow, to predict the closing price of BTC using the past rolling-window of 10 days worth of crypto pricing. 

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

