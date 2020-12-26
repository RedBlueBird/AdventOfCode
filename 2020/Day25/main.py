from math import ceil, floor
import datetime as dt
now = dt.datetime.now()

a = 5290733
b = 15231938

ans1 = 0

i = 0 
while (pow(7,i,20201227) != a):
    i += 1 

ans1 = pow(b,i,20201227)


print("Part 1: ", ans1)
print("Time : ", dt.datetime.now()-now)