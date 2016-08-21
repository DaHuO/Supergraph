def sleep(n):
    N = n
    s = {'0','1','2','3','4','5','6','7','8','9'}
    while len(s) != 0:
        s = s.difference({x for x in str(N)})
        N = N + n
    return N - n
    
f0 = open('A-large.in','r')
f1 = open('outLarge.txt','w')
T = int(f0.readline())
ansL = []
for t in range(T):
    n = int(f0.readline())
    if n==0:
        ansL.append('INSOMNIA')
    else:
        ansL.append(sleep(n))
for t in range(T):
    print(ansL[t])
    f1.write('Case #'+str(t+1)+': '+str(ansL[t])+'\n')
f0.close()
f1.close()

