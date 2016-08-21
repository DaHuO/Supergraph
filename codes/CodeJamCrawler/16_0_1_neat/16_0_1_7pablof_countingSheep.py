import re
##f = open('test.in')
##f = open('A-small-attempt0.in')
f = open('A-large.in')
f2 = open('file.txt','w')
numset = set('0123456789')
T = f.readline()
i = 0
for l in f:
    i += 1
    if(int(l) == 0):
        print("Case #" + str(i) + ": INSOMNIA",file=f2)
        continue
    x = 0
    d = set()
    while(True):
        x += 1
        n = str(x * int(l))
        d.update(set(n))
        if(len(numset - d) == 0):
            print("Case #" + str(i) + ": " + n,file=f2)
            break
f.close()
f2.close()
