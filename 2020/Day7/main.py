from math import ceil 
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

i = 0

bags = {}
connections1 = {}
connections2 = {}

c = 0
while i < n:
    sentence = text[i][:-1].split(", ")
    contain = " ".join(sentence[0].split(" ")[:2])
    sentence[0] = " ".join(sentence[0].split(" ")[4:])
    
    if contain not in bags:
        bags[contain] = c 
        c += 1
    
    if text[i].split(" ")[4] != "no":
        k = [" ".join(j.split(" ")[1:3]) for j in sentence]
        counts = [int(j.split(" ")[0]) for j in sentence]
        for j in k:
            if j not in bags:
                bags[j] = c
                c += 1 
    
        for j in k:
            if bags[j] not in connections1:
                connections1[bags[j]] = []
            connections1[bags[j]].append(bags[contain])
        
        connections2[bags[contain]] = [[bags[j],counts[x]] for x, j in enumerate(k)]
    else:
        connections2[bags[contain]] = []
        
    i += 1
    
convert = [0 for i in range(len(bags))]
for i in bags:
    convert[bags[i]] = i
ans1 = []

def dfs1(node, connections1):
    ans1.append(convert[node])
    
    if node not in connections1:
        return
    for i in connections1[node]:
        dfs1(i, connections1)
        
def dfs2(node, connections2):
    if node not in connections2 or len(connections2[node]) == 0:
        return 1
    return sum([dfs2(i, connections2)*j for i,j in connections2[node]])+1

dfs1(bags['shiny gold'], connections1)


print("Part 1: ", len(set(ans1))-1)
print("Part 2: ", dfs2(bags['shiny gold'], connections2)-1)