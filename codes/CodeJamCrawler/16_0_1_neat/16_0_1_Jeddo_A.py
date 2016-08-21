def count(N):
    if N==0:
        return 'INSOMNIA'
    seen =[]
    for d in str(N):
        seen.append(d)
    seen= list(set(seen))
    i = 2
    while len(seen)<10:
        for d in str(i*N):
            seen.append(d)
        seen = list(set(seen))
        i +=1
    return N*(i-1)

inf = open('A-large.in','r')
out = open('A-large.out','w')

T = int(inf.readline())
for i in range(1,T+1):
    N = int(inf.readline())
    out.write('Case #'+str(i)+': '+str(count(N))+'\n')
out.close()
inf.close()
