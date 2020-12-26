from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')
cin = open("codes.txt", "r")

text = [str(i) for i in fin.read().splitlines()]
codes = [str(i) for i in cin.read().splitlines()]

n = len(text)
m = len(codes)
mem = [[] for i in range(n)]
source = [0,0]

ans1 = 0
ans2 = 0 

i = 0
while i < n:
    k = text[i]
    index = int(k.split(": ")[0])
    if text[i].split(": ")[1] == '"a"':
        source[0] = index
        mem[index] = "a"
        i += 1
        continue
    elif text[i].split(": ")[1] == '"b"':
        source[1] = index
        mem[index] = "b"
        i += 1
        continue
    rules = text[i].split(": ")[1].split(" | ")
    mem[index] = [[int(h) for h in j.split(" ")] for j in rules]
    i += 1

def find(string, index):
    if len(string) < 1:
        return [[False, string]]
    if index in source:
        if string[0] == mem[index]:
            if len(string) == 1:
                return [[True, ""]]
            return [[True, string[1:]]]
        return [[False, string]]
    
    output = []
    for h in mem[index]:
        substr = [string]
        newsub = []
        for j in h:
            for k in substr:
                a = find(k,j)
                for b in a:
                    if b[0]:
                        newsub.append(b[1])
            substr,newsub = newsub,[]
        for j in substr:
            output.append([True,j])
    if output != []:
        return output
    return [[False, string]]
        
def search():
    ans = 0
    for k in codes:
        a = find(k, 0)
        for b in a:
            if b[0] and len(b[1]) < 1:
                ans += 1 
                break
    return ans

ans1 = search()
mem[8] = [[42],[42,8]]
mem[11] = [[42,31],[42,11,31]]
ans2 = search()

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)