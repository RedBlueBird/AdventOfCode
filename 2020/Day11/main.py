from math import ceil 
fin = open("input.txt", 'r')

text = ["." + i + "." for i in fin.read().splitlines() ]
text = [[j for j in i] for i in text]

n = len(text) + 2
m = len(text[0])

state1 = [['.' for i in range(m)]] + text + [['.' for i in range(m)]]
state2 = [[i for i in j] for j in state1]

changes = True
while changes:
    changes = False
    for i, x in enumerate(state1):
        for j, y in enumerate(x):
            if i == 0 or i == n-1:
                continue
            if j == 0 or j == m-1:
                continue
            occupied = 0
            occupied += 1 if state1[i-1][j] == "#" else 0
            occupied += 1 if state1[i+1][j] == "#" else 0
            occupied += 1 if state1[i][j-1] == "#" else 0
            occupied += 1 if state1[i][j+1] == "#" else 0
            occupied += 1 if state1[i-1][j-1] == "#" else 0
            occupied += 1 if state1[i+1][j-1] == "#" else 0
            occupied += 1 if state1[i-1][j+1] == "#" else 0
            occupied += 1 if state1[i+1][j+1] == "#" else 0
            if state1[i][j] == "L" and 0 == occupied:
                state2[i][j] = "#"
                changes = True
            elif state1[i][j] == "#" and occupied >= 4:
                state2[i][j] = "L"
                changes = True
    state1 = [[j for j in i] for i in state2]


ans1 = sum([1 for i in state1 for j in i if j == "#"])


state1 = [['.' for i in range(m)]] + text + [['.' for i in range(m)]]
state2 = [[i for i in j] for j in state1]

changes = True
while changes:
    changes = False
    for i, x in enumerate(state1):
        for j, y in enumerate(x):
            if i == 0 or i == n-1:
                continue
            if j == 0 or j == m-1:
                continue
            occupied = 0
            a,b = i,j
            while a < n-1:
                a += 1 
                if state1[a][b] == '#':
                    occupied += 1
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while a > 0:
                a -= 1 
                if state1[a][b] == '#':
                    occupied += 1 
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while b > 0:
                b -= 1 
                if state1[a][b] == '#':
                    occupied += 1 
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j 
            while b < m-1:
                b += 1 
                if state1[a][b] == '#':
                    occupied += 1 
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while a < n-1 and b < m-1:
                b += 1 
                a += 1 
                if state1[a][b] == '#':
                    occupied += 1
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while a > 0 and b < m-1:
                b += 1 
                a -= 1 
                if state1[a][b] == '#':
                    occupied += 1
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while a < n-1 and b > 0:
                b -= 1 
                a += 1 
                if state1[a][b] == '#':
                    occupied += 1 
                    break
                elif state1[a][b] == "L":
                    break
            a,b = i,j
            while a > 0 and b > 0:
                b -= 1 
                a -= 1 
                if state1[a][b] == '#':
                    occupied += 1
                    break
                elif state1[a][b] == "L":
                    break
            if state1[i][j] == "L" and 0 == occupied:
                state2[i][j] = "#"
                changes = True
            elif state1[i][j] == "#" and occupied >= 5:
                state2[i][j] = "L"
                changes = True
    state1 = [[j for j in i] for i in state2]
    
ans2 = sum([1 for i in state1 for j in i if j == "#"])

print("Part 1: ", ans1)
print("Part 2: ", ans2)
