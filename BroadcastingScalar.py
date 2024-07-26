# Broadcasting with a scalar
# Example1
import  numpy as np
arr=np.array([10,11,12,13])
value=5
result=arr+value
print(result)

# Example2
import numpy as np
arr1=np.array([[0,1,2],[3,4,5]])
arr2=np.array([1,2,3])
result=arr1+arr2
print(result)

# Example3
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([1,2,3,4])
# result=arr1+arr2
# print(result)


# Example4
import numpy as np
arr1=np.array([[0,1,2],[3,4,5]])
arr2=np.array([[1],[2]])
result=arr1+arr2
print(result)