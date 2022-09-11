import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./loan_data_set.csv')
data.head()
data_original=data.copy()
data.to_string(index=False)

num_col=['LoanAmount','Loan_Amount_Term','Credit_History']
for m in data.columns:
    for n in num_col:
        if n == m:
            data.fillna(data[n].mean(),inplace=True)
            print()

print("\nLoan Amount info:")
data['LoanAmount'].info()
print("")
print("LoanAmount mean:",data['LoanAmount'].mean())
print("")
print("Loan_Amount_Term Mean:",data['Loan_Amount_Term'].mean())
print("")
print("Credit_History Mean:",data['Credit_History'].mean())
data.head()