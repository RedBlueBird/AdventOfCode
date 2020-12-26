from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

ans1 = 0
ans2 = 0 

ingredients = []
allergy = []
ingredCode = {}
allergyCode = {}
c = 0
d = 0
i = 0
while i < n:
    k = text[i].split(" (contains ")
    ingredients.append(k[0].split(" "))
    allergy.append(k[1][:-1].split(", "))
    for x,j in enumerate(ingredients[-1]):
        if j not in ingredCode:
            ingredCode[j] = c
            c += 1 
        ingredients[-1][x] = ingredCode[j]
    for x,j in enumerate(allergy[-1]):
        if j not in allergyCode:
            allergyCode[j] = d
            d += 1
        allergy[-1][x] = allergyCode[j]
    i += 1
ingredConv = ["" for i in range(c)]
allergyConv = ["" for i in range(d)]
for i in ingredCode:
    ingredConv[ingredCode[i]] = i
for i in allergyCode:
    allergyConv[allergyCode[i]] = i

identify = [[j for j in range(c)] for i in range(d)]
for x,i in enumerate(ingredients):
    for y,j in enumerate(allergy[x]):
        identify[j] = list(set(identify[j]).intersection(set(i)))

listed = []
for i in identify:
    listed.extend(i)
listed = list(set(listed))

for i in ingredients:
    for j in i:
        if j not in listed:
            ans1 += 1

listed = [[allergyConv[i]] for i in range(d)]
result = [12,85,98,52,82,19,20,22]
for x,i in enumerate(listed):
    listed[x].append(ingredConv[result[x]])
listed.sort()
ans2 = ",".join([i[1] for i in listed][:])

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)