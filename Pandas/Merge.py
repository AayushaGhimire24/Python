import pandas as pd
data1={'StudentID':[101,102,103],'Name':['Ram','Hari','Sita']}
data2={'StudentID':[101,102,104],'City':['Ktm','Bkt','Pkr']}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

# Merging using inner-Inner Joins
df3=df1.merge(df2,on='StudentID',how='inner')
print(df3)

# Merging using left-Left  Joins
df4=df1.merge(df2,on='StudentID',how='left')
print(df4)
# Merging using right-Right Joins
df5=df1.merge(df2,on='StudentID',how='right')
print(df5)