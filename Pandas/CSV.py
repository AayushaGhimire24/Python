import pandas as pd
data={
    'Id':[101,102,103,104,105],
    'Name':['Ram','Hari','Sita','Rita','Ravi'],
    'Age':[25,24,26,27,25],
    'Salary':[25000,24000,26000,27000,25000]
}
df=pd.DataFrame(data)
df.to_csv('record.csv',index=False)

# Appending to a CSV file
data={
    'Id':[106,107],
    'Name':['Puja','Rajeev'],
    'Age':[20,21],
    'Salary':[20000,21000]
}
df=pd.DataFrame(data)
df.to_csv('record.csv',mode='a',header=False,index=False)

# Reading a CSV file
import pandas as pd
df=pd.read_csv('record.csv')
print(df)