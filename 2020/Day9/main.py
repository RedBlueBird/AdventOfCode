from math import ceil 
fin = open("input.txt", 'r')

text = [int(i) for i in fin.read().splitlines()]

n = len(text)
ans1 = 0 
ans2 = 0 

i = 25
while i < n:
    sums = text[i]
    maps = {}
    valid = False
    for k in text[i-25:i]:
        if sums - k in maps:
            valid = True
            break
        else:
            maps[k] = 0
    i += 1
    if valid == False:
        ans1 = sums
        break
    

for x,i in enumerate(text):
    sums = i
    valid = False
    for y, j in enumerate(text):
        if y > x:
            sums += j
        if sums == 105950735:
            ans2 = min(text[x:y]) + max(text[x:y])
            valid = True
            break
    if valid:
        break
    
print("Part 1: ", ans1)
print("Part 2: ", ans2)
    
            