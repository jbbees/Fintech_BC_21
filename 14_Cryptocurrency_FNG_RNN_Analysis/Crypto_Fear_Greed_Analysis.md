# Bitcoin Fear & Greed Index, Price Predictions

We're using time-series BTC price data from the Fear & Greed (FNG) Index of crypto prices. We will be building a deep RNN model utilizing long short-term memory (LSTM) architecture within keras tensorflow, to predict the closing price of BTC using the past rolling-window of 10 days worth of crypto pricing. 


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
