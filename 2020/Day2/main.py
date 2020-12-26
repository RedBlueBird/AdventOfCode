from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

ans1 = 0
ans2 = 0 

i = 0
while i < n:
    k = text[i].split(": ")
    string = k[1]
    k = k[0].split(" ")
    a = k[1]
    ranges = [int(j) for j in k[0].split("-")]
    c = 0
    for j in string:
        if j == a:
            c += 1 
    if ranges[0] <= c <= ranges[1]:
        ans1 += 1
    c = 0
    if string[ranges[0]-1] == a:
        c += 1 
    if string[ranges[1]-1] == a:
        c += 1 
    if c == 1:
        ans2 += 1
    i += 1 

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)