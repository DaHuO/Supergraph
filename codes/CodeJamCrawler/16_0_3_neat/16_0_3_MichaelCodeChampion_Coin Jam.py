#Coin Jam
import random

file = open('Input_CoinJamSmall.txt', 'r')

for i in next(file).split():
    length = int(i)
x = []
for line in file:
    for i in line.split():
        x.append(int(i))

# create 'small' jamcoins
out = open('Output_CoinJamSmall.txt', 'w')
out.write('Case #1:\n')
N = x[0]
J = x[1]

n = pow(2, N-1) + 1  #smallest possible number
done = 0
while done < J:
    if n/2 == round(n/2):
        n = n+1
    bn = bin(n)
    y = [0]*9
    z = 0
    act = 0
    for i in range(9):
        z = (int(bn[2:], i+2))
        # try 1000 numbers randomly
        for j in range(1000):
            r = round(random.random()*100)+2
            if z/r == round(z/r) and r < z:
                y[i] = r
                act = i
                break
        if y[act] == 0:
            break
    good = 0
    for q in range(9):
        if y[q] > 0:
            good += 1
    if good == 9:
        out.write('%s %d %d %d %d %d %d %d %d %d\n' % (bn[2:], y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8]) )
        done += 1

    n += 1



