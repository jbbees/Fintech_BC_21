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

We are predicting Yen values from years 2018 and onward (dependent y values) based on past Yen values 2017 are previous (independent X features). 

1. Create a train/test split. The training in-sample data is rows from 2017 and previous. The testing holdout data is rows 2018 and above. 
<pre><code>train = yen_futures[:'2017']
test = yen_futures['2018':]
</code></pre>

2. Create four unique dataframes, 2 for training, 2 for testing. We will put the X components into a dataframe using `to_frame()`
<pre><code>X_train = train['Lagged_Return'].to_frame()             # Lagged Return is the independent component. 
y_train = train['Return']                               # Return is the dependent component, it's what we're trying to predict. 
X_test = test['Lagged_Return'].to_frame() 
y_test =test['Return']
</code></pre>

3. Analyze the `X_train` data. This is 967 rows of the 1,415 rows.

<details><summary>X_train</summary>

![image](images/rg_3_xtrain.PNG)
    
</details>

# Build the Linear Regression Model

1. Import the `sklearn` module
<pre><code>from sklearn.linear_model import LinearRegression</code></pre>

2. Build the model and fit with only the **training** data `X_train` and `y_train`
<pre><code>model = LinearRegression()
model.fit(X_train, y_train)
</code></pre>
