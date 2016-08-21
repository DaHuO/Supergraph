import os

target = list([str(x) for x in range(10)])
inf = open('input.in','r')
inp = inf.read().split('\n')
inf.close()
outf = open('output','w')
T = int(inp.pop(0))
for i in range(T):
    N = int(inp.pop(0))
    ships = list()
    asleep = False
    for j in range(1,101):
        ships += list(str(j*N))
        ships = list(set(ships))
        if len(filter(lambda x:x not in ships, target))==0:
            outf.write('Case #%d: %d\n'%(i+1, j*N))
            asleep = True
            break
    if not asleep:
        outf.write('Case #%d: INSOMNIA\n'%(i+1))
outf.close()
