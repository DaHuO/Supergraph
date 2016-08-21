# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
filein = open('2016QB.in', 'r')
fileout = open('2016QB.out', 'w')

T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    cakes = list(filein.readline().rstrip())
    cakes.reverse()
    ans = 0
    upside = '+'
    for i in range(len(cakes)):
        if cakes[i] != upside:
            upside = '-' if upside == '+' else '+'
            ans += 1
    fileout.write(str(ans) + '\n')

filein.close()
fileout.close()
