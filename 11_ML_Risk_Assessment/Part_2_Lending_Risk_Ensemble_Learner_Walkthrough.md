# Risky Business Part 2 - Ensemble Learner Walkthrough

**CODER'S NOTE:** This notebook will not be able to exdecute the RF model results. When running tests on predictions and scoring, python returns sample inconsistency error:  

> ValueError: Found input variables with inconsistent numbers of samples: [17205, 51612]

The core problem lies in the data file itself. There's too many columns to process even after data-cleaning. The solution file to this homework used a completely different data file, so I am not able to rely on the provided solution. 

The code below however, is the appropriate steps as to how you setup a Random Forest analysis.


This part is more advanced. Instead of predicting loan default based on resampling data classes, we'll use an ensemlbe-learner, tree-algorithim to breakdown the data and make the prediction. Will a tree algorithm be better suited for predicting loan risk?

## Imports
<pre><code>import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.ensemble import BalancedRandomForestClassifier
from imblearn.ensemble import EasyEnsembleClassifier
</code></pre>

## Data Pre-Processing

Read-in data file. This will use more detailed loan data than the previous section. 

<pre><code>file_path = Path('resources/LoanStats_2019Q1.csv')
df = pd.read_csv(file_path, skiprows=1)[:-2]
df.head()
</code></pre>

#### Part 1: Eliminate useless columns.

First, drop useless columns that will have no predictive value. Try to get rid of as many columns with *non-numeric* values. The columns to drop have the **same value for every row**. 

For example, the column `pymnt_plan` denoting a loan applicant is on a payment plan, has only the value 'n' for all rows. So no loan applicants regardless the risk are on a payment plan, so this column can be eliminated. Other columns to drop are based on personal decision.

<pre><code>df.drop('pymnt_plan', axis=1, inplace=True ) # this column only has 1 value for every row. value 'n', no applicants are on a pymt plan. Useless column.
df.drop('hardship_flag', axis=1, inplace=True)          # all rows under column have the same value, meaningless.
df.drop('debt_settlement_flag', axis=1, inplace=True)   # all rows have same value. no predictive characteristic. 
df.drop('recoveries', axis=1, inplace=True)             # same value.
df.drop('collection_recovery_fee', axis=1, inplace=True)
df.drop('acc_now_delinq', axis=1, inplace=True)
df.drop('num_tl_120dpd_2m', axis=1, inplace=True)
df.drop('num_tl_30dpd', axis=1, inplace=True)
df.drop('num_tl_90g_dpd_24m', axis=1, inplace=True)
df.drop('tax_liens', axis=1, inplace=True) 
df.drop('issue_d', axis=1, inplace=True)                # the loan issue date is meaningless.
df.drop('next_pymnt_d', axis=1, inplace=True)           # next payment date is meaningless.
</code></pre>

#### Part 2: Label Encoding

Second, make a list of all columns with non-numeric values that will need to be transformed with a `LabelEncoder()`.
<pre><code>target_cols = ['home_ownership', 'verification_status', 'pymnt_plan', 'hardship_flag', 'debt_settlement_flag']
</code></pre>

Create a `LabelEncoder()` object
<pre><code>from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
</code></pre>

Loop through the list of target columns, fit the LabelEncoder with the column, and then transform the value to numeric.
<pre><code>
for col in target_cols:
	
    label_encoder.fit(df[col])
    
    df[col] = label_encoder.transform(df[col])
</code></pre>

#### Part 3: Define X features & y-target vector.

<pre><code>y = df['loan_status']
X = df.copy()
X.drop('loan_status', axis=1, inplace=True)
</code></pre>

#### Part 4: Train/test split.

<pre><code>from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
</code></pre>

#### Part 5: Scaling the feature data.

Create a `StandardScaler()` object, and fit with only numeric valued data. It cannot accept non-numeric. And then use our X_scaler to scale the X features data.

<pre><code>from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
</code></pre>

## Balanced Random Forest Classifier
Build the RF model and fit.
<pre><code>from imblearn.ensemble import BalancedRandomForestClassifier
brf = BalancedRandomForestClassifier(n_estimators=100, random_state=1)
brf.fit(X_train_scaled, y_train)
</code></pre>

Make predictions.
<pre><code>y_pred_brf = brf.predict(X_train_scaled)</code></pre>

**NOTE:** This notebook will not be able to exdecute the RF model results. When running tests on predictions and scoring, python returns sample inconsistency error:  
> ValueError: Found input variables with inconsistent numbers of samples: [17205, 51612]
The core problem lies in the data file itself. There's too many columns to process even after data-cleaning. The solution file to this homework used a completely different data file, so I am not able to rely on the provided solution. 

The code below however, is the appropriate steps as to how you setup a Random Forest analysis.
