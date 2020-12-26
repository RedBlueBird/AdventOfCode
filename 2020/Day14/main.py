from math import floor
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)
ans1 = 0
ans2 = 0

mem1 = {}
mem2 = {}
i = 0

mask = ""
while i < n:
    if text[i][:4] == "mask":
        mask = text[i].split(" ")[2]
        i += 1
        continue
    address = int(text[i].split(" ")[0][4:-1])
    num = int(text[i].split(" ")[2])
    oldNum = num
    
    newNum = [0 for i in range(36)]
    c = 1
    while num:
        newNum[-c] = num%2
        num = num >> 1 
        c += 1
    for x, bit in enumerate(mask):
        if bit == "0":
            newNum[x] = 0
        if bit == "1":
            newNum[x] = 1
    num = 0
    for bit in newNum:
        num = (num << 1) + bit
    mem1[address] = num
    
    newAdd = [0 for i in range(36)]
    perm = []
    c = 1 
    while address:
        newAdd[-c] = address%2 
        address = address >> 1 
        c += 1 
    for x, bit in enumerate(mask):
        if bit == "1":
            newAdd[x] = 1
        elif bit == "X":
            newAdd[x] = -1
            perm.append(x)
 
    allAdd = []
    def broadcast(perms, curr):
        lists = []
        if len(perms):
            curr[perms[0]] = 0
            lists.extend([k[:] for k in broadcast(perms[1:], curr)])
            curr[perms[0]] = 1 
            lists.extend([k[:] for k in broadcast(perms[1:], curr)])
            return lists
        else:
            lists.append(curr)
            return lists
    allAdd = broadcast(perm,newAdd)
    
    for add in allAdd:
        newAdd = 0
        for bit in add:
            newAdd = (newAdd << 1) + bit
        mem2[newAdd] = oldNum
    i += 1

for j in mem1:
    ans1 += mem1[j]

for j in mem2:
    ans2 += mem2[j]

print("Part 1: ", ans1)
print("Part 2: ", ans2)