import sys
f=open('A-large.in')
g=open('Result.in','w')
T=int(f.readline())
for i in range(T):
    N=f.readline().strip()
    if (N == '0'):
        g.write('Case #'+str(i+1)+': INSOMNIA\n')
    else:
        numbers=set(N)
        nN = int(N)
        cN = nN
        for j in range(sys.maxsize//nN):
            cN = cN+nN
            numbers = numbers.union(set(str(cN)))
            if len(numbers)==10:
                break
        if len(numbers)==10:
            g.write('Case #'+str(i+1)+': '+str(cN)+'\n')
        else:
            g.write('Case #'+str(i+1)+': INSOMNIA\n')
        
g.close()
f.close()
