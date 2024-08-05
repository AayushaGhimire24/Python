import pandas as pd
Data={'A':[11,12,13,14,15],
      'B':[16,17,18,19,20],
      'C':[21,22,23,24,25]}
df=pd.DataFrame(Data,index=['a','b','c','d','e'])
# print the dataframe
print(df)

# Positional Indexing using iloc
print(df.iloc[0])

# Label Based Indexing using loc
print(df.loc['b'])

# Boolean Indexing
print(df[df['A']>13])