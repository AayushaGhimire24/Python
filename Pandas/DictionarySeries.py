# A dictionary can also be used to create Series. The key used in dictionary acts as a named index/label
import pandas as pd
scores={"BIM5":4,"BIM4":7,"BIM3":8}
myvar=pd.Series(scores)
print(myvar)

# Using only the selected items to create a series
import pandas as pd
scores={"BIM5":4,"BIM4":7,"BIM3":8}
myvar=pd.Series(scores,index=['BIM5','BIM4'])
print(myvar)