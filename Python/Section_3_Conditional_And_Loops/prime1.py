import time
start_time = time.time()
num =6
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")

end_time = time.time()
print("Start Time:", start_time)
print("End Time:", end_time)
print("Total Duration (seconds):", end_time - start_time)