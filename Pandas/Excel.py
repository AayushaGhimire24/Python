import pandas as pd
df=pd.read_excel('Employee.xlsx')
# print all data
print(df)

# print only top 5 rows
print(df.head())

# print only top 2 rows
print(df.head(2))

# print only last 5 rows
print(df.tail())

# print only last 3 rows
print(df.tail(3))

# print data of name column only
print(df['Name'])

# print data of multiple columns
print(df[['Name','Salary']])

# to remove duplicate records
df1=df.drop_duplicates()
print(df1)

# to fill custom value in empty(missing) cells
df2=df.fillna("Missing")
print(df2)

# to drop(remove) records with missing values
df3=df.dropna()
print(df3)