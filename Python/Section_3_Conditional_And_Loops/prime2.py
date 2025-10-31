import time
import math

start_time = time.time()

num=6

for num in range(2,int(math.sqrt(num))):
    if num%2==0:
        print("Not Prime")
        break
else:
    print("Prime")

end_time = time.time()

print("Start Time:", start_time)
print("End Time:", end_time)
print("Total Duration (seconds):", end_time - start_time)