from math import ceil 
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]
rounds = 6

ans1 = 0
ans2 = 0

act1 = {}
act2 = {}

for i,x in enumerate(text):
    for j,y in enumerate(x):
        if y == "#":
            act1[(0,i,j)] = 0

for itr in range(rounds):
    inact = {}
    for z,x,y in act1:
        counts = 0
        for i in [x,x-1,x+1]:
            for j in [y,y-1,y+1]:
                for k in [z,z-1,z+1]:
                    if i == x and j == y and k == z:
                        continue
                    if (k,i,j) in act1:
                        counts += 1
                        continue
                    if (k,i,j) in inact:
                        inact[(k,i,j)] += 1 
                        if inact[(k,i,j)] == 3:
                            act2[(k,i,j)] = 0
                        elif inact[(k,i,j)] == 4:
                            del act2[(k,i,j)]
                    else:
                        inact[(k,i,j)] = 1
        if counts in [2,3]:
            act2[(z,x,y)] = 0
    act1,act2 = act2,act1
    act2 = {}

ans1 = len(act1)


act1 = {}
act2 = {}

for i,x in enumerate(text):
    for j,y in enumerate(x):
        if y == "#":
            act1[(0,0,i,j)] = 0
    
for itr in range(rounds):
    inact = {}
    for w,z,x,y in act1:
        counts = 0
        for i in [x,x-1,x+1]:
            for j in [y,y-1,y+1]:
                for k in [z,z-1,z+1]:
                    for h in [w,w-1,w+1]:
                        if i == x and j == y and k == z and h == w:
                            continue
                        if (h,k,i,j) in act1:
                            counts += 1
                            continue
                        if (h,k,i,j) in inact:
                            inact[(h,k,i,j)] += 1 
                            if inact[(h,k,i,j)] == 3:
                                act2[(h,k,i,j)] = 0
                            elif inact[(h,k,i,j)] == 4:
                                del act2[(h,k,i,j)]
                        else:
                            inact[(h,k,i,j)] = 1
        if counts in [2,3]:
            act2[(w,z,x,y)] = 0
    act1,act2 = act2,act1
    act2 = {}

ans2 = len(act1)

    
print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now() - now)