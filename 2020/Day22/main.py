from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("player1.txt", 'r')
cin = open("player2.txt", "r")

txt1 = [int(i) for i in fin.read().splitlines()]
txt2 = [int(i) for i in cin.read().splitlines()]
player1 = [i for i in txt1]
player2 = [i for i in txt2]

ans1 = 0
ans2 = 0 

while len(player1) != 0 and len(player2) != 0:
    if player1[0] < player2[0]:
        player1,player2 = player2,player1
        
    player1.append(player1.pop(0))
    player1.append(player2.pop(0))
if len(player2) != 0:
    player1 = player2

ans1 = sum([i * (len(player1)-x) for x,i in enumerate(player1)])


player1 = [i for i in txt1]
player2 = [i for i in txt2]

def game(p1, p2, depth=0):
    p1 = [i for i in p1]
    p2 = [i for i in p2]
    history = [[p1[:],p2[:]]]
    print(depth)
    while len(p1) != 0 and len(p2) != 0:
        win = True
        
        if p1[0] <= len(p1)-1 and p2[0] <= len(p2)-1:
            win = game(p1[1:p1[0]+1], p2[1:p2[0]+1],depth+1)[0]
        elif p1[0] < p2[0]:
            win = False
            
        if win:
            p1.append(p1.pop(0))
            p1.append(p2.pop(0))
        else:
            p2.append(p2.pop(0))
            p2.append(p1.pop(0))

        if [p1,p2] in history:
            return [True, p1]
        history.append([p1[:],p2[:]])
    if len(p1) != 0:
        return [True,p1]
    return [False,p2]
    
result = game(player1, player2)[1]
ans2 = sum([i * (len(result)-x) for x,i in enumerate(result)])

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)