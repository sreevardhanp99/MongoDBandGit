from numpy import *

arr1 =  array([
    [1,2,3],
    [4,5,6]
])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()
print(arr2)

arr3 = arr1.reshape(3,2)
print(arr3)

arr4 = arange(1,13)
print(arr4)

arr5 = arr4.reshape(3,4)
print(arr5)

arr6 = arr4.reshape(2,2,3)
print(arr6)

arr7 = arr4.reshape(2,3,2)
print(arr7)

m1 = matrix('1 2 3;4 5 6;7 8 9')
print(m1)

m2 = matrix('1 2; 3 4; 5 6')
print(m2)

print(diagonal(m1))

print(max(m1))