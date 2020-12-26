from math import ceil 
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)
ans1 = 0
ans2 = 1
classes = 20

ranges = [[int(k) for k in j.split("-")] for i in text[:classes] for j in i.split(": ")[1].split(" or ")]
ran = [[[int(k) for k in j.split("-")] for j in i.split(": ")[1].split(" or ")] for i in text[:classes]]
convert = [-1 for i in range(classes)]
main = [101,179,193,103,53,89,181,139,137,97,61,71,197,59,67,173,199,211,191,131]
groups = [[] for i in range(classes)]
cand = [[] for i in range(classes)]

def check(k):
    valid = False
    for x in ranges:
        if x[0] <= k <= x[1]:
            valid = True
    return valid

def con(k, p):
    possible = []
    for q, x in enumerate(ran):
        valid = False
        for i in k:
            valid = False
            for y in x:
                if y[0] <= i <= y[1]:
                    valid = True
                    break
            if not valid:
                break
        if valid:
           possible.append(q)
    return possible

def define(k, p):
    for q, x in enumerate(ran):
        if q in convert:
            continue
        valid = False
        for i in k:
            valid = False
            for y in x:
                if y[0] <= i <= y[1]:
                    valid = True
                    break
            if not valid:
                break
        if valid:
           convert[p] = q
           break

# i-th q is the i-th class in the text 
# p is the #th in the ticket

i = classes
while i < n:
    ticket = eval("[" + text[i] + "]")
    error = sum([j for j in ticket if not check(j)])
    if error:
        ans1 += error
    else:
        for p, j in enumerate(ticket):
            groups[p].append(j)
    i += 1

for p,q in enumerate(groups):
    cand[p] = con(q,p)
    
prior = sorted([[len(p),q] for q, p in enumerate(cand)])
for i in prior:
    define(groups[i[1]],i[1])

for x,y in enumerate(convert):
    if 0 <= y <= 5:
        ans2 = ans2 * main[x]


print("Part 1: ", ans1)
print("Part 2: ", ans2)