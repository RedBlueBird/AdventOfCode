from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

ans1 = 1
ans2 = 0 

tiles = {}

def rotate(tile):
    newt = [i[:] for i in tile] 
    lens = len(tile)
    for i,x in enumerate(tile):
        for j,y in enumerate(x):
            newt[j][lens-i-1] = tile[i][j]
    return newt

def findedge(tile):
    edges = []
    for i in range(4):
        edges.append([tile[0]])
        tile = rotate(tile)
    for i in range(4):
        edges[i].append(edges[i][0][::-1])
    return edges

i = 0
while i < n:
    key = int(text[i].split(" ")[1][:-1])
    tile = []
    for j in range(1,11):
        tile.append([k for k in text[i+j]])
    tiles[key] = tile
    i += 12

corner = [1093, 2111, 3709, 3457]
edge = [3347, 3191, 2837, 2333, 2593, 2089, 1373, 1553, 3643, 2621, 3187, 3137, 3907, 3919, 2129, 1367, 2417, 1871, 3209, 2971, 2963, 3229, 1429, 1193, 1327, 1723, 2549, 1321, 1987, 2503, 1783, 2269, 2897, 1531, 2857, 2789, 3049, 1013, 3631, 1789]
middle = [3329, 2131, 3331, 1657, 3079, 3623, 1879, 1549, 2477, 3089, 3607, 3119, 1823, 3931, 2081, 2243, 1831, 1579, 3373, 2141, 3343, 2357, 2953, 3011, 1861, 2909, 2887, 2633, 1997, 3767, 3917, 2677, 1123, 2389, 3929, 3163, 1117, 2399, 3371, 2659, 1171, 2833, 1129, 1103, 1901, 3389, 1979, 2707, 3701, 2153, 1973, 2683, 3989, 2113, 2699, 1933, 1423, 3217, 3221, 2969, 3739, 3449, 3491, 1907, 1699, 2221, 1361, 3571, 3251, 3253, 1609, 3001, 2749, 1217, 1481, 1741, 1613, 1489, 3539, 1439, 1493, 3323, 1753, 2267, 3319, 1303, 1249, 3673, 2791, 1319, 2029, 1277, 3313, 1619, 2803, 1747, 2039, 1031, 3583, 1237]
# for i in tiles:
#     counts = 0
#     a = findedge(tiles[i])
#     for j in tiles:
#         if i != j:
#             match = False
#             b = findedge(tiles[j])
#             for ai, x in enumerate(a):
#                 for bi, y in enumerate(b):
#                     if x[0] in y or x[1] in y:
#                         match = True
#                         break
#                 if match:
#                     break
#             if match:
#                 counts += 1
#     if counts == 2:
#         ans1 = ans1 * i
#         corner.append(i)
#     elif counts == 3:
#         edge.append(i)
#     else:
#         middle.append(i)

imap = [[0 for i in range(12)] for i in range(12)]





print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)