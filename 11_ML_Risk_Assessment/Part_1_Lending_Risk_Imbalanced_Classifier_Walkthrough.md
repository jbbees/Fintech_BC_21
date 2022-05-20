![image](images/credit-risk.jpg)

# Part 1: Lending Club Loan Risk Analysis - Imbalanced Classification (Supervised ML)

<details><summary>Premise:</summary>
  
We are dealing an **imbalanced classification problem** for predicting risk of default on bank loan applications based on dataset attributes (borrower's income, total debt they have, derogatory marks on their credit record, number of financial accounts, or if they own their current home), using various ML algorithms. Loans will be either classified as *low-risk* of defaulting or *high-risk* of defaulting. We don't know what would a be a good method to make this determination. We will use different ML methods to feed the data into these models that will predict the rish of loan default. More specifiically we will explore two broad ML methods: Oversampling & Ensemble Random Forest Classifier.

</details>

<details><summary>What does the file contain?</summary>

A very basic file containing over 70,000 loan applications with few descriptive columns. The data is imbalanced. There are way more low-risk loans than high-risk. The attributes of the file contain:

* loan_size (or principal amount)
* interest_rate
* homeowner_status (own, rent, or buy, this column will need to be converted to a numeric form with label encoding)
* borrowers_income
* number_of_accounts
* derogatory_marks
* total_debt
* debt_to_income
* loans_status (default predictive target, two classes: low-risk or high-risk)

</details>


The raw data file has very basic data. 

The key column we care about is 

The typical 

Predictive value 

## Imports

We'll be using both scikit-learn and imblearn feature suites.

<pre><code>import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import ClusterCentroids
from imblearn.combine import SMOTEENN
</code></pre>

## Pre-Processing Data

Read-in data. This is a very basic loan data file.
<pre><code>file_path = Path('resources/lending_data.csv')
df = pd.read_csv(file_path)
df.head()
</code></pre>

#### Part 1: Label Encoding of non-numeric columns.

Classification models work off of numeric data. Any columns with character values need be converted to numeric values using a **LabelEncoder** object to input into a classifier. **NOTE:** Before doing this, it's easier to first assess if the column has a predictive value, and if it doesn't simply drop the column. However, in our case the non-numeric columns are `homeowner` and `loan_status` which is the target prediction, so these columns have to remain, and need to be converted to numeric format.

Import the feature and create the object.

`from sklearn.preprocessing import LabelEncoder`
`label_encoder = LabelEncoder()`




#### Part 2: Define X predictive features, & y-target vector. 

Our y-target is what will be the **TRUE POSITIVE** event in our confusion matrix. We are predicting *low-risk* loans. Only 1 column in the dataset reflects this attribute, the `loan_status` column.
`y = df['loan_status']`

The X features will be everything else except `loan_status`. We'll copy the original dataframe into X and drop the target column, and any column that doesn't have predictive value.
<pre><code>X = df.copy() 
X.drop('loan_status', axis=1, inplace=True)
</code></pre>

#### Part 3: Train/test split
<pre><code>X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
</code></pre>

#### Part 4: Scale the training data.

Create a `StandardScaler` object, fit the training data to it, and then transform the X FEATURES data that will be exposed to the models.  
<pre><code>
data_scaler = StandardScaler()
X_scaler = data_scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
</code></pre>

## ML Model Comparisons. Which predicts best? Imblanced data model or resampled data model? 

We are building four comparative Logistic Regression models to predict/classify **high risk loans** with the imbalanced dataset. We are deciding if a *basic* ML model (Logistical Regression) with an *imbalanced* dataset will predict risky loans better than a ML model with a *resampled* dataset that eliminates bias. There will be 1 control model with imbalanced data. And we will build three different models that resample the loan classes differently. This means we will resample using a oversampling algorithm (SMOTE), undersampling (Clustered Centroids), and combination sampling (SMOTEENN). We'll bring the imblearn features to use these algos. 

### MODEL 1: Logistic Regression Model - Imbalanced Data

The control model. A basic algorithm predicts fraud on imbalanced data. That is, we're not resampling the data. 

Our imbalanced y-target data shows way more low-risk loans than high-risk ones.
<pre><code>y.value_counts()</code></pre>
>low_risk     75036
>high_risk     2500

We'll use **scikit learn** features to import in the LR. We'll use a seed state value of 1 to replicate results. And fit the regular training data on it. No resampling or scaling. 

<pre><code> from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(solver='lbfgs', random_state=1)
lr_model.fit(X_train, y_train)
</code></pre>

Make predictions. Run an accuracy score on how well an LR model predicted. It displayed a **95%** balanced accuracy score.
<pre><code>from sklearn.metrics import balanced_accuracy_score
y_pred_lr = lr_model.predict(X_test)
balanced_accuracy_score(y_test, y_pred_lr)
</code></pre>
>0.9520479254722232

Display a confusion matrix to breakdown the True Positives (acutal high-risk loans) and True Negatives (actual low-risk loans)
<pre><code>from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_lr)
cm_df = pd.DataFrame(
    cm,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']
)
cm_df
</code></pre>

Run an imblanced classification report on the precision and recall performances. 

<pre><code>from imblearn.metrics import classification_report_imbalanced
print(classification_report_imbalanced(y_test, y_pred_lr))
</code></pre>

After we cleaned the imbalanced loan dataset. We will re-sampled the cleaned training data acorss three different ML models. In this case an oversampler, an undersampler, and a combination re-sampler. We first create each resampling model. And then resample the imbalanced training data. And then we will fit that resampled onto a Logistic Regression Model, and then run predictions model scoring. 

### MODEL 2: SMOTE Oversampler

**NOTE:** I did include a naive overslampling model, but SMOTE oversampling works better.

The second model will oversample the *minority* data class of high-risk loans to match the *majority* class of low-risk using SMOTE algorithm.

Bring the **imblearn** feature-suite to use the SMOTE resampling algo. Fit resample the training data with SMOTE. Keep a seed value of 1. 
<pre><code>from imblearn.over_sampling import SMOTE
X_resampled_sm, y_resampled_sm = SMOTE(random_state = 1, sampling_strategy = 1.0).fit_resample(X_train, y_train)
</code></pre>

After resampling the class breakdown in the data both classes are equal. We boosted the high-risk numbers.
<pre><code>Counter(y_resampled_sm)</code></pre>
>Counter({'low_risk': 56271, 'high_risk': 56271})

Fit the SMOTE resampled training data to our second Logistic Regression model.
<pre><code>sm_model = LogisticRegression(solver='lbfgs', max_iter =2000, random_state=1)
sm_model.fit(X_resampled_sm, y_resampled_sm)
</code></pre>

Make predictions. Get the accuracy score. The SMOTE oversampling has a **99%**  balanced accuracy score. Better than our basic imbalanced model. 
<pre><code>y_pred_sm = sm_model.predict(X_test)
balanced_accuracy_score(y_test, y_pred_sm)
</code></pre>
>0.9936781215845847

Display a confusion matrix.
<pre><code>cm_sm = confusion_matrix(y_test, y_pred_sm)
cm_sm_df = pd.DataFrame(
    cm_sm,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']
)
cm_sm_df
</code></pre>

Display an imbalanced classification report. 
<pre><code>print(classification_report_imbalanced(y_test, y_pred_sm))</code></pre>

### MODEL 3: Unsampling Model - Clustered Centroids

This resampling model will undersample the *majority* class of low-risk loans to match the *minority* class of high-risk loans. 

Bring in the Clustered Centroids algo. Create a Clustered Centroid object. Resample the training data.
<pre><code>from imblearn.under_sampling import ClusterCentroids
cc = ClusterCentroids(random_state = 1)
X_resampled_cc, y_resampled_cc = cc.fit_resample(X_train, y_train)
</code></pre>

After resampling the data, the target class breakdown shows this. We decreased the large number of low-risk loans. 
<pre><code>Counter(y_resampled_cc)</code></pre>
>Counter({'high_risk': 1881, 'low_risk': 1881})

Fit the Clustered Centroid resampled data to our third Logistic Regression model.
<pre><code>cc_model = LogisticRegression(solver = 'lbfgs', random_state = 1)
cc_model.fit(X_resampled_cc, y_resampled_cc)
</code></pre>

Make predictions. Display balanced accuracy score of **98.6%**. It performed marginally weaker than the SMOTE model, but still better than our control model.
y_pred_cc = cc_model.predict(X_test)
balanced_accuracy_score(y_test, y_pred_cc)
>0.9865149130022852

Display confusion matrix.
<pre><code>cm_cc = confusion_matrix(y_test, y_pred_cc)
cm_cc_df = pd.DataFrame(
    cm_cc,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']
)
cm_cc_df
</code></pre>

Display the imabalanced classification report.
<pre><code>print(classification_report_imbalanced(y_test, y_pred_cc))</code></pre>

### MODEL 4: Combination Sampling Model - SMOTEENN

Final model will combine oversampling and undersampling. SMOTEENN will first oversample the *minority* class of high risk loans to match the low-risk one's. And then the **Editied Nearest Neighbors**, the ENN part, feature kicks in. It will undersample the balanced dataset, by eliminating data points it feels are too close. 

Bring in SMOTEENN algo. Create a SMOTEENN object and fit resample the imbalanced training data.
<pre><code>from imblearn.combine import SMOTEENN
cos = SMOTEENN(random_state = 1)
X_resampled_cos, y_resampled_cos = cos.fit_resample(X_train, y_train)
</code></pre>

The resampling yields a slightly uneven breakdown. This will give a good chance of non-biased classification.
<pre><code>Counter(y_resampled_cos)</code></pre>
>Counter({'high_risk': 55603, 'low_risk': 55948})

Fit the SMOTEENN resampled data to the final Logistic Regression.
<pre><code>cos_model = LogisticRegression(solver = 'lbfgs', random_state = 1)
cos_model.fit(X_resampled_cos, y_resampled_cos) 
</code></pre>

Make predictions. Get the balanced accuracy score. The final score is **99.3%** which is better than the Clustered Centroids model, and better than the control model. 
<pre><code>y_pred_cos = cos_model.predict(X_test)
balanced_accuracy_score(y_test, y_pred_cos)
</code></pre>
>0.9935182494822666

Display the confusion matrix.
<pre><code>cm_cos = confusion_matrix(y_test, y_pred_cos)
cm_cos_df = pd.DataFrame(
    cm_cos,
    index = ['Actual 0', 'Actual 1'],
    columns = ['Predicted 0', 'Predicted 1']
)
cm_cos_df
</code></pre>

Display the classification report.
<pre><code>print(classification_report_imbalanced(y_test, y_pred_cos))</code></pre>
