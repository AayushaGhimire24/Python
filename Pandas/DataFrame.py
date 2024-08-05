# Create a simple pandas DataFrame
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
# Load data into a dataFrame object
df=pd.DataFrame(data)
print(df)


# Using named indexing
df=pd.DataFrame(data,index=['x','y','z'])
print(df)


# Loading file into dataframe
