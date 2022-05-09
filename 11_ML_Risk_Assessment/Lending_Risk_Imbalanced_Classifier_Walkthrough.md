

We are dealing an imbalanced classification problem for predicting if loan applications based on data are low-risk of defaulting or high-risk of defaulting. We don't know what would a be a good method to make. 

The data is imbalanced. There are way more low-risk loans than high-risk, but that imbalance



The raw data file has very basic data. 

The key column we care about is 

The typical 

Predictive value 


# OPTION 1: Resampling Method with various ML algorithms. 

This approach uses algorithms that will be taking the loan-level data file, focusing on the core columns that have a predictive relevance, splitting the targer vector (loan_status) into two classes: *low-risk*, or *high-risk*. And then re-balancing those the data in those classes  to make them equal.   



# OPTION 2: Ensemble Random Forest algorithm.

This approach will take the loan file and have the algorithm determine on its own  which attributed 
