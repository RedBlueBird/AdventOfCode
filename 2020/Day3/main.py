from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

ans1 = 0
ans2 = 0 

def trees(dx, dy):
    n = len(text)
    m = len(text[0])
    i = 0
    x = 0
    result = 0
    while i < n:
        if text[i][x] == "#":
            result += 1 
        x = (x+dx)%m
        i += dy
    return result

ans1 = trees(3,1)
ans2 = trees(1,1)*trees(3,1)*trees(5,1)*trees(7,1)*trees(1,2)

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)