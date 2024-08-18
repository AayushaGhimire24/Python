# Create a csv file "emp.csv" to store id, name, address, salary of 5 employees.
import pandas as pd
data={
    'Id':[101,102,103,104,105],
    'Name':['Ram','Hari','Sita','Rita','Ravi'],
    'Age':[25,24,26,27,25],
    'Salary':[25000,24000,26000,27000,25000]
}
df=pd.DataFrame(data)
df.to_csv('emp.csv',index=False)
