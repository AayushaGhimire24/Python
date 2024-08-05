# Create a simple Pandas series from a list
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)


# Named index(labeled) can also be created
myvar=pd.Series(a,index=['a','b','c'])
print(myvar)