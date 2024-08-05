import pandas as pd
Data={'A':[11,12,13,14,15],
      'B':[16,17,18,19,20],
      'C':[21,22,23,24,25]}
df=pd.DataFrame(Data,index=['a','b','c','d','e'])
# print the dataframe
print(df)

# Positional Slicing using iloc
print(df.iloc[1:4,1:3])

#   Label based slicing using loc
print(df.loc['b':'d','B':'C'])

# Boolean Slicing
print(df[df['A']>13])

print(df[df['A']>13]&[df['B']<19])

