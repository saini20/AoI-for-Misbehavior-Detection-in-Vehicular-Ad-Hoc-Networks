import random
import math
import time

# generate random number of cars (between 1 and 10)
n=30
num_cars = random.randint(1, n)

# generate generation times for each car (exponential distribution with lambda = 0.5)
gen_times = [random.expovariate(0.5) for i in range(num_cars)]

# print out the results
i=1
count=0
queue=[]
for t in gen_times:
   if t<4:

       count=count+1
       print(t)
       time.sleep(random.randint(1,3))




   i=i+1
print("Number of cars:", count)
