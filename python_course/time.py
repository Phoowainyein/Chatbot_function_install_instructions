#! /usr/bin/python3
import time
start_time = time.time()
for x in range(10):
    for y in range(10):
        xy = x+y
        #print(xy)
end_time = time.time()
print(" ")
print(end_time - start_time)

time_now=time.time()
print(time_now)
time.ctime(time_now)
