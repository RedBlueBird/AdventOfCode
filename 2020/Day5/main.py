from math import ceil 
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)
ans1 = 0
ans2 = 0

seats = []

for i in text:
    a, b = 0, 127
    row, col = 0, 0
    for k in i[:7]:
        if k == "B":
            a += ceil((b-a)/2)
        else:
            b -= ceil((b-a)/2)
    row = a
    a, b = 0, 7
    for k in i[7:]:
        if k == 'R':
            a += ceil((b-a)/2)
        else:
            b -= ceil((b-a)/2)
    col = a
    ids = row * 8 + col
    ans1 = max(ids,ans1)
    seats.append(ids)

for i in seats:
    if i + 1 not in seats and i + 2 in seats:
        ans2 = i + 1

print("Part 1: ", ans1)
print("Part 2: ", ans2)