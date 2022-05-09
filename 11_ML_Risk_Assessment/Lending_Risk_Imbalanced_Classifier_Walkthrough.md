
<details><summary>Premise:</summary>
  
We are dealing an **imbalanced classification problem** for predicting risk of default on bank loan applications, based on the supplemental loan application attributes (borrower's income, total debt they have, derogatory marks on their credit record, number of financial accounts, or if they own their current home), using various ML algorithms. Loans will be either classified as *low-risk* of defaulting or *high-risk* of defaulting. We don't know what would a be a good method to make this determination. We will use different ML methods to feed the data into these models that will predict the rish of loan default. More specifiically we will explore two broad ML methods: Oversampling & Ensemble Random Forest Classifier.

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


# OPTION 1: Resampling Method with various ML resampling algorithms. 

This approach uses algorithms that will be taking the loan-level data file, focusing on the core columns that have a predictive relevance, splitting the targer vector (loan_status) into two classes: *low-risk*, or *high-risk*. And then re-balancing those the data in those classes  to make them equal.   



# OPTION 2: Ensemble Random Forest algorithm.

This approach will take the loan file and have the algorithm determine on its own  which attributed 
