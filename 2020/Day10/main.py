from math import ceil 
fin = open("input.txt", 'r')

text = [int(i) for i in fin.read().splitlines()]

text.append(0)
text.sort()
text.append(text[-1]+3)
n = len(text)

jolts = [0,0,0]
ans1, ans2 = 0, 0


i = 1
while i < n:
    jolts[text[i] - text[i-1]-1] += 1 
    i += 1 
ans1 = jolts[2]*jolts[0]

dp = [0 for i in range(n)]
dp[0] = 1
i = 1
while i < n:
    if text[i]-1 in text:
        dp[i] += dp[text.index(text[i]-1)]
    if text[i]-2 in text:
        dp[i] += dp[text.index(text[i]-2)]
    if text[i]-3 in text:
        dp[i] += dp[text.index(text[i]-3)]
    if text[i] == 0:
        text[i] = text[i-1]
    i += 1
ans2 = dp[-1]


print("Part 1: ", ans1)
print("Part 2: ", ans2)
