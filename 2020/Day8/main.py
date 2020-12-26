from math import ceil 
fin = open("input.txt", 'r')

text = [str(i).split(" ") for i in fin.read().splitlines()]

n = len(text)

ans1 = 0
ans2 = 0

nop = []
jmp = []
for x, i in enumerate(text):
    if i[0] == "nop":
        nop.append(x)
    elif i[0] == "jmp":
        jmp.append(x)

for i in jmp:
    text[i][0] = "nop"
    tracker = 0
    ans1 = 0
    visited = [False for i in range(n)]
    while True:
        if visited[tracker]:
            break
        visited[tracker] = True
        if text[tracker][0] == 'nop':
            tracker += 1 
        elif text[tracker][0] == "acc":
            ans1 += int(text[tracker][1])
            tracker += 1 
        elif text[tracker][0] == "jmp":
            tracker += int(text[tracker][1])
        if tracker == n:
            ans2 = ans1
            break
    text[i][0] = "jmp"
    if ans2 != 0:
        break

if ans2 == 0 and False:
    for i in nop:
        text[i][0] = "jmp"
        tracker = 0
        ans1 = 0
        visited = [False for i in range(n)]
        while True:
            if visited[tracker]:
                break
            visited[tracker] = True
            if text[tracker][0] == 'nop':
                tracker += 1 
            elif text[tracker][0] == "acc":
                ans1 += int(text[tracker][1])
                tracker += 1 
            elif text[tracker][0] == "jmp":
                tracker += int(text[tracker][1])
            if tracker == n:
                ans2 = ans1
                break
        text[i][0] = "nop"
        if ans2 != 0:
            break

tracker = 0
ans1 = 0
visited = [False for i in range(n)]
while True:
    if visited[tracker]:
        break
    visited[tracker] = True
    if text[tracker][0] == 'nop':
        tracker += 1 
    elif text[tracker][0] == "acc":
        ans1 += int(text[tracker][1])
        tracker += 1 
    elif text[tracker][0] == "jmp":
        tracker += int(text[tracker][1])

print("Part 1: ", ans1)
print("Part 2: ", ans2)