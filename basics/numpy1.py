import numpy as np
# 1D Numpy Arrays
arr1= np.array([1,2,3])
arr2= np.array([2,3,4])

print(arr1 + arr2)
print(arr1.mean())
print(type(arr1))


# 2D Numpy Array

arr3= np.array([
    [1,2,3],
    [2,3,4]
])

print(arr3.shape)
print(arr3.ndim)
print(arr3.size)
print(arr3.dtype)