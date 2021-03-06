# Risky Business Part 2 - Ensemble Learner Walkthrough

This part is more advanced. Performing more *supervised* ML techniques on a complex imbalanced dataset. We'll be a using quarterly data from Lending Club that has way more detailed characteristics for loan applications for high or low risk of default. Instead of predicting loan default based on resampling data classes, we'll use an ensemlbe-learner, tree-algorithim to breakdown the heavily imbalanced data and make the predictions using the various columns and characteristics of the dataset. We will use two decision tree ML algos: an Balanced Random Forest and an Easy Ensemble Classifier.

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

**NOTE:** We are not resampling the imbalanced data when training our ML models. We will rely on ML to determine which column features to use to classify.

Build the RF model and fit.
<pre><code>from imblearn.ensemble import BalancedRandomForestClassifier
brf = BalancedRandomForestClassifier(n_estimators=100, random_state=1)
brf.fit(X_train_scaled, y_train)
</code></pre>

Make predictions.
<pre><code>y_pred_brf = brf.predict(X_train_scaled)</code></pre>

Find the accuracy score on the predictions
<pre><code>balanced_accuracy_score(y_test, y_pred_brf)</code></pre>
> **Balanced Accuracy Score: 0.699176962831924**

Confusion matrix.
<pre><code>cm = confusion_matrix(y_test, y_pred_brf)
cm_df = pd.DataFrame(
    cm,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']
)
cm_df
</code></pre>
![image](images/cm_brf.PNG)

Classification report.
<pre><code>print(classification_report_imbalanced(y_test, y_pred_brf))</code></pre>
![image](images/cr_brf.PNG)

Display feature importances. These are the core features in the data the RF algo determined for the final predictions, for every row, loan application, or in this case the `root node` and split up into various `decision nodes` leading down to the `terminal node` to classify a single loan as high risk/low risk.

Put feature importances into a dataframe. Reverse sort so the highest weight indicates the core features that make up the decision to label risk.
<pre><code>
brf_importances_df = pd.DataFrame(
    sorted(zip(brf.feature_importances_, X.columns), reverse=True)
)
brf_importances_df
</code></pre>

Do additional stripping of the features dataframe.
<pre><code>brf_importances_df.set_index(brf_importances_df[1], inplace=True)
brf_importances_df.drop(columns=1, inplace=True)
brf_importances_df.rename(columns = {0: 'Feature Importances'}, inplace=True)
</code></pre>

Display the ten most important features in a visual graph. I chose a horizontal bar graph.
<pre><code>brf_importances_df[:10].plot(
    kind='barh',
    color='lightgreen',
    title = 'Feature Importances',
    legend = False
)</code></pre>

![image](images/brf_feature_importances_sorted.PNG)

## Easy Ensemble Classifier

We'll just repeat the same steps for this RF model.
<pre><code>from imblearn.ensemble import EasyEnsembleClassifier
ens = EasyEnsembleClassifier(n_estimators=100, random_state=1)
ens.fit(X_train_scaled, y_train)
</code></pre>

Make predictions.
<pre><code>y_pred_ens = ens.predict(X_train_scaled)</code></pre>

Accuracy score, confusion matrix, and classification report.
<pre><code>balanced_accuracy_score(y_test, y_pred_ens)

cm2 = confusion_matrix(y_test, y_pred_ens)
cm2_df = pd.DataFrame(
    cm2,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']   
)
cm2_df

print(classification_report_imbalanced(y_test, y_pred_ens))
</code></pre>
> **Balanced accuracy score: 0.7393285341162741**

![image](images/cm_ens.PNG)

![image](images/cr_ens.PNG)

## Conclusion
Both decision tree models performed horribly. And I mean horribly. But I can't make a comparison of which ML method (decision tree vs resampling) is good because we used different datasets. But with this dataset, I wouldn't rely or have any confidence to use either of these models, based on the data file given, to train a ML algo to predict loan risk. 

When we did the first part with resampling techniques, we a had basic file with few columns, and we resampled the training data for each instance. In this ensemble-learner section we're not resampling anything, it'll be the ML algo making it's decision on what's in the file. Because this is supervised machine learning, and a very big data file of lots of characteristics, the effectiveness of the model results and errors are tied to my data cleaning decisions, and elimination of columns. I cleaned the file of columns I felt were not predictive based on the fact the same value exists across all rows. 

The Balanced Forest Classifier, looking at the feature importances, based its decisions primarily on `loan amount`, `loan payment amount`, `loan payment`. A lot of False Negatives were seen in the holdout data. As noted in the code, 19% of the low-risk loans were classified as high-risk despite the overwhelming low-risk population in the test data. What could account for this? Maybe if the loan application type is not an independent loan. Most of the loan data were indivdual loans, but some were joint-types. What's even worse is that high-risk loans represented only .006% of the holdout data, and 41% of high-risk loans were classified as low-risk. So this model barely captures high-risk loans accurately.

The Easy Ensemble Classifier performed better in terms of correctly classifying high-risk loans, but more low-risk loans were classed as high-risk of default. 
