from math import ceil 
fin = open("input.txt", 'r')

text = [0,8,15,2,12,1,4]
mem = {i:[x+1,x+1] for x,i in enumerate(text)}
turn = len(text)+2
mem[0] = [1,turn-1]
num = 0
ans1 = 0 
ans2 = 0

while turn <= 30000000:
    if num in mem:
        num = mem[num][-1] - mem[num][-2]
    else:
        num = 0
    if num in mem:
        mem[num].append(turn)
        mem[num].pop(0)
    else:
        mem[num] = [turn, turn]
    turn += 1 
    if turn == 2020:
        ans1 = num
    if turn == 30000000:
        ans2 = num

print("Part 1: ", ans1)
print("Part 2: ", ans2)