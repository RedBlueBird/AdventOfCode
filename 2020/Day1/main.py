from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [int(i) for i in fin.read().splitlines()]

n = len(text)

ans1 = 0
ans2 = 0 

for i in text:
    for j in text:
        if i + j == 2020:
            ans1 = i * j 
            break
    if ans1 != 0:
        break

for i in text:
    for j in text:
        for h in text:
            if i + j + h == 2020:
                ans2 = i * j * h 
                break
        if ans2 != 0:
            break
    if ans2 != 0:
        break


print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)