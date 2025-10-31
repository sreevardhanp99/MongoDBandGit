from array import *

arr1 = array('i',  [1,2,3,4,-5])

print(arr1.buffer_info())

arr2 = array(arr1.typecode,[a*a for a in arr1])

print(arr2)