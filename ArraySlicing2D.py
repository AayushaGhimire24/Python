# From the second element(row), slice elements from index 1 to index 4(not included):
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])

# From both elements, return index 2
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])

# We can also use slicing to modify array elements
import numpy as np
arr=np.array([1,2,3,4,5])
arr[:3]=25
print(arr)