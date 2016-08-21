import sys 
from sets import Set

lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    n = int(lines[i+1].strip())
    if n == 0: print 'Case #'+str(i+1)+': INSOMNIA'
    else:
        k = 0
        d = Set()
        while(len(d) < 10):
            k += 1
            d.update(list(str(n*k)))
        print 'Case #'+str(i+1)+': '+str(n*k)
