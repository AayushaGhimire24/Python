# Using Lexsort
import numpy as np
surname=('Airee','Kami','Khadka')
firstname=('Dipendra','Sompal','Paras')
ind=np.lexsort((surname,firstname))
print(ind)
arr=[firstname[i]+" "+ surname[i] for i in ind]
print(arr)