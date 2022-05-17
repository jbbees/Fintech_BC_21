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

## Pre-Processing Data

The loan-level dataset will be cleaned to be able to feed into the various high-level models.

#### Part 1: Label Encoding of non-numeric columns.

Classification models work off of numeric data. Any columns with character values need be converted to numeric values using a **LabelEncoder** object to input into a classifier. **NOTE:** Before doing this, it's easier to first assess if the column has a predictive value, and if it doesn't simply drop the column. However, in our case the non-numeric columns are `homeowner` and `loan_status` which is the target prediction, so these columns have to remain, and need to be converted to numeric format.

Import the feature and create the object.

`from sklearn.preprocessing import LabelEncoder`
`label_encoder = LabelEncoder()`




#### Part 1: Define X predictive features, & y-target vector. 

Our y-target is what will be the **TRUE POSITIVE** event in our confusion matrix. We are predicting *high-risk* loans that would default or be a loss to the firm. Only 1 column in the dataset reflects this attribute * 

#### Part 2: 

## Create a base Logistic Regression Model

After we cleaned the imbalanced loan dataset. We will re-sampled the cleaned training data with three different ML models. In this case an oversampler, an undersampler, and a combination re-sampler. We first create each resampling model. And then resample the imbalanced training data. And then we will fit that resampled onto a Logistic Regression Model. 

We'll use **scikit learn** features ro

<pre><code>
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(solver='lbfgs', random_state=1)
lr_model.fit(X_train, y_train)
</code></pre>

## MODEL 1: SMOTE Oversampler

This approach uses algorithms that will be taking the loan-level data file, focusing on the core columns that have a predictive relevance, splitting the targer vector (loan_status) into two classes: *low-risk*, or *high-risk*. And then re-balancing those the data in those classes  to make them equal.   

## MODEL 2: Unsampling Model - Clustered Centroids

## MODEL 3: Combination Sampling Model - SMOTEENN
