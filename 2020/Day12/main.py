from math import ceil 
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

x = 0 
y = 0
points = [[1,0],[0,-1],[-1,0],[0,1]]
point = 0

for i in text:
    direction = i[0]
    dist = int(i[1:])
    if direction == "N":
        y += dist 
    if direction == "S":
        y -= dist
    if direction == "E":
        x += dist 
    if direction == "W":
        x -= dist
    if direction == "F":
        x += dist * points[point][0]
        y += dist * points[point][1]
    if direction == "R":
        point = (point+int(dist/90))%4
    if direction == "L":
        point = (point-int(dist/90))%4

ans1 = abs(x) + abs(y)

wayx = 10
wayy = 1
x = 0 
y = 0

for i in text:
    direction = i[0]
    dist = int(i[1:])
    if direction == "N":
        wayy += dist 
    if direction == "S":
        wayy -= dist
    if direction == "E":
        wayx += dist 
    if direction == "W":
        wayx -= dist
    if direction == "F":
        x += dist * wayx
        y += dist * wayy
    if direction == "R" and dist == 90 or direction == "L" and dist == 270:
        wayx,wayy = wayy,-wayx
    if direction == "R" and dist == 180 or direction == "L" and dist == 180:
        wayx,wayy = -wayx,-wayy
    if direction == "R" and dist == 270 or direction == "L" and dist == 90:
        wayx,wayy = -wayy,wayx

ans2 = abs(x) + abs(y)

print("Part 1: ", ans1)
print("Part 2: ", ans2)
    