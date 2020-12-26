import datetime as dt
now = dt.datetime.now()
from collections import defaultdict
from itertools import product

fin = open("input.txt", 'r')
text = [str(i) for i in fin.read().splitlines()]


black = set()

ans1 = 0 
ans2 = 0

for line in text:
    r, c = 0, 0
    it = iter(line.strip())
    while True:
        try:
            i = next(it)
            if i in "ns": i += next(it)
        except StopIteration:
            break

        if i == "e": r += 1
        if i == "w": r -= 1
        if i == "se": c += 1
        if i == "nw": c -= 1
        if i == "sw":
            r -= 1
            c += 1
        if i == "ne":
            r += 1
            c -= 1

    if (r, c) in black:
        black -= {(r, c)}
    else:
        black |= {(r, c)}

ans1 = len(black)

for i in range(100):
    neighbors = defaultdict(int)

    for r, c in black:
        neighbors[r, c]
        for dq, dr in product(range(-1, 2), repeat=2):
            if dq == dr: continue
            neighbors[r + dq, c + dr] += 1

    for p, n in neighbors.items():
        if p in black and not 1 <= n <= 2:
            black -= {p}
        if p not in black and n == 2:
            black |= {p}
ans2 = len(black)


print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)