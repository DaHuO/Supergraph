import math

data = open("A-large.in").read().split()
n = data[0]
data = map(int, data[1:])
answ = []

for t in data:
    num = [0]*10
    if t == 0:
        answ.append('INSOMNIA')
    else:
        mul = 1
        while not all(num):
            g = t*mul
            while g > 0:
                num[g%10] = 1
                g /= 10
            mul += 1
        answ.append((mul-1)*t)

with open("A-large.out", 'w') as f:
    for i,o in enumerate(answ):
        f.write("Case #{}: {}\n".format(i+1, o))
