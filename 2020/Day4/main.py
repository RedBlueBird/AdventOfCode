from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]
types = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
ports = []

n = len(text)

ans1 = 0
ans2 = 0 

i = 0
while i < n:
    k = ""
    while i < n and text[i] != "":
        k += text[i] + " "
        i += 1
    i += 1 
    k = {j.split(":")[0]:j.split(":")[1] for j in k[:-1].split(" ")}
    ports.append(k)

def check(passport):
    for i in types:
        if i not in passport and i != 'cid':
            return False
    return True
    
ports = [i for i in ports if check(i)]
ans1 = len(ports)

def checkagain(passport, head):
    if head == 'cid':
        return True
    k = passport[head]
    if head == 'byr':
        return 1920 <= int(k) <= 2002
    elif head == 'iyr':
        return 2010 <= int(k) <= 2020
    elif head == 'eyr':
        return 2020 <= int(k) <= 2030
    elif head == 'hgt':
        unit = k[-2:]
        if unit not in ['cm','in']:
            return False
        k = int(k[:-2])
        if unit == 'cm':
            return 150 <= k <= 193
        else:
            return 59 <= k <= 76
        return False
    elif head == "hcl":
        if len(k) != 7:
            return False
        if k[0] != "#":
            return False
        for i in k[1:]:
            if i not in '0123456789abcdef':
                return False
        return True
    elif head == 'ecl':
        return k in ['amb','blu','brn','gry','grn','hzl','oth']
    else:
        if len(k) != 9:
            return False
        for i in k:
            if i not in '0123456789':
                return False
        return True
    return False

ports = [i for i in ports if sum([1 for j in types if checkagain(i,j)])==len(types)]
ans2 = len(ports)

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)