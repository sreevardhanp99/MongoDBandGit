from numpy import *

arr1 = array([1,2,3,4])
print(arr1)

arr2 = array([5,6,7,8], float)
print(arr2)
print(arr2.dtype)

arr3 =linspace(0,16,17)
print(arr3)

arr4 = linspace(0,16)
print(arr4)

arr5 = arange(1,16)
print(arr5)

arr6 = arange(1,16,2)
print(arr6)

arr7 = logspace(1,40,5)
print(arr7)

arr8 = zeros(5)
print(arr8)

arr9 = zeros(5,int)
print(arr9)

arr10 = ones(5)
print(arr10)