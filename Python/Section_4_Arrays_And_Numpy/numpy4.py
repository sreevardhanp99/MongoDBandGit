from numpy import *

# aliasing
arr1 = array([1,2,3,4,5])
arr2 = arr1

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

print("===============================")
# shallow copy
arr3 = array([6,7,8,9,10])
arr4 = arr3.view()

arr3[0] = 100
print(arr3)
print(arr4)


print(id(arr3))
print(id(arr4))


# deep copy
print("===============================")
arr5 = array([11,12,13,14,15])
arr6 = arr5.copy()
arr5[0] = 200

print(arr5)
print(arr6)

print(id(arr5))
print(id(arr6))