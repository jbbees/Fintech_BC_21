# Risky Business Part 2 - Ensemble Learner Walkthrough



This part is more advanced. Instead of predicting loan default based on resampling data classes, we'll use an ensemlbe-learner, tree-algorithim to breakdown the data and make the prediction. Will a tree algorithm be better suited for predicting loan risk?

## Data Pre-Processing

This will use more detailed loan data than the previous section. 

<pre><code>file_path = Path('resources/LoanStats_2019Q1.csv')
df = pd.read_csv(file_path, skiprows=1)[:-2]
df.head()
</code></pre>

#### Part 1: Label Encoding

First, dropping columns I feel will have no predictive value. The `issue_d` column has no impact on the outcome. 
<pre><code>df.drop('issue_d', axis = 1, inplace=True)</code></pre>

Second, make a list of all columns that will need to be transformed.
<pre><code>target_cols = ['home_ownership', 'verification_status', 'pymnt_plan', 'hardship_flag', 'debt_settlement_flag']
</code></pre>

Third, create a `LabelEncoder()` object
<pre><code>from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
</code></pre>

Fourth, loop through the list of target columns, fit the LabelEncoder with the column, and then transform the value to numeric.
<pre><code>
for col in target_cols:
	
    label_encoder.fit(df[col])
    
    df[col] = label_encoder.transform(df[col])
</code></pre>

#### Part 2: Define X features & y-target vector

<pre><code>y = df['loan_status']
X = df.copy()
X.drop('loan_status', axis=1, inplace=True)
</code></pre>
