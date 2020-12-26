from math import floor
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

time = int(text[0])
bus = [int(i) for i in text[1].split(",") if i != "x"]

ans1 = 0

dist = 1000

for i in bus:
    lower = floor(time/i)
    mins = lower*i+i-time
    if (dist > mins):
        ans1 = mins * i 
        dist = mins

def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 
  
def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 
  
def crt(m, x): 
    while True: 
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] +  modinv(m[0],m[1]) * x[1] * m[0] 
        temp2 = m[0] * m[1] 
  
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  
  
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
  
        if len(x) == 1: 
            break
  
    return x[0] 

remainder = [-i for i, j in enumerate(text[1].split(",")) if j != "x"]


print("Part 1: ", ans1)
print("Part 2: ", crt(bus,remainder))
