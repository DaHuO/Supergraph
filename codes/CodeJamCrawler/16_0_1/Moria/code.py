def myfunc(t):
    p=list(str(1234567890))
    count=1
    while (len(p)>0):
        a=t*count
        a1=list(str(a))
        p=list(set(p)-set(a1))
        count=count+1
    return a

f=open('A-large.in','r')
g=open('output.txt','w')
nt=int(f.readline().strip())
for i in range(nt):
    t=int(f.readline().strip())
    if t==0:
        txt='Case #{0}: {1}'.format(i+1,'INSOMNIA')
        g.write(txt)
        g.write('\n')
    else:
        m=myfunc(t)
        txt='Case #{0}: {1}'.format(i+1,str(m))
        g.write(txt)
        g.write('\n')
g.close()
f.close()