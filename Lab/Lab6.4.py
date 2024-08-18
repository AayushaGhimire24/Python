# Read from "emp.csv" and display records of only those whose salary is more than 35000.
import pandas as pd
pd.options.display.max_rows=5
df=pd.read_csv('emp.csv')
result=df[df['Salary']>25000]
print(result)