from math import ceil, floor
import datetime as dt
now = dt.datetime.now()

k = [int(i) for i in "389125467"]

ans1 = ""
ans2 = 0 

def destination(curr, start):
    curr = [i for i in curr]
    if start < min(curr):
        start = max(curr)
        return curr.index(start)
    while start not in curr:
        start -= 1 
    return curr.index(start)

for c in range(10):
    ind = 0
    out = k[ind+1:ind+4]
    print(k)
    print(out)
    print(ind)
    print(c)
    start = k[ind]-1
    nexts = k[(ind+4)%len(k)]
    
    k = k[:ind+1] + k[ind+4:]
    target = destination(k, start)
    k = k[:target+1] + out + k[target+1:]
    
    ind = k.index(nexts)
    k = k[ind+1:] + k[:ind+1]

i = (k.index(1)+1)%len(k)
while i < len(k)*2:
    if k[i % len(k)] == 1:
        break
    ans1 += str(k[i%len(k)])
    i += 1
    

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)