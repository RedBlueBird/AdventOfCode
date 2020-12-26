from math import ceil 
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]
text.append("")

n = len(text)

i = 0
part1 = 0 
part2 = 0

while i < n:
    k = text[i]
    a = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    response1 = []
    response2 = set(a[j] for j in text[i])
    
    while k != "":
        k = text[i]
        if k == "":
            i += 1 
            continue
        response1.extend([a[j] for j in k])
        response2 = response2.intersection(set(a[j] for j in k))
        i += 1

    part1 += len(set(response1))
    part2 += len(response2)

print("Part 1: ", part1)
print("Part 2: ", part2)
        