import numpy as np
arr=np.array([11,21,34,44,55])
values=[25,46]
i=np.searchsorted(arr,values)
print(i)