
<details><summary>Premise:</summary>
We are dealing an imbalanced classification problem for predicting if bank loan applications based on column data will be *low-risk* of defaulting or *high-risk* of defaulting. We don't know what would a be a good method to make this determination. We will use different ML methods to feed the data into these models that will predict the rish of loan default. More specifiically we will explore two broad ML methods: Oversampling & Ensemble Random Forest Classifier.

The data is imbalanced. There are way more low-risk loans than high-risk, but that imbalance


</details>


The raw data file has very basic data. 

The key column we care about is 

The typical 

Predictive value 


# OPTION 1: Resampling Method with various ML algorithms. 

This approach uses algorithms that will be taking the loan-level data file, focusing on the core columns that have a predictive relevance, splitting the targer vector (loan_status) into two classes: *low-risk*, or *high-risk*. And then re-balancing those the data in those classes  to make them equal.   



# OPTION 2: Ensemble Random Forest algorithm.

This approach will take the loan file and have the algorithm determine on its own  which attributed 
