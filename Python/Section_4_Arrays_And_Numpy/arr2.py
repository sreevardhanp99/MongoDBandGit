from array import *

arr = array('i',[])

n = int(input("Enter number of elements:"))

for i in range(n):
    x=int(input("Enter the elements:"))
    arr.append(x)
print(arr)

index = 0
val=int(input("Enter the element to be searched:"))
for v in arr:
    if v==val:
        print("Found at index:",index)
        break
    index+=1
else:
    print("Not Found")


print(arr.index(val))