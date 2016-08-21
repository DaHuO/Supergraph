fi=open('A-large.in')
fo=open('answer.out','w')
t=int(fi.readline())
ans=[]
for i in range(1,t+1):
    s=set()
    n=int(fi.readline())
    if n==0: ans+=[''.join(['Case #',str(i),': INSOMNIA'])]
    else:
        s|=set(str(n))
        m=1
        while len(s)<10:
            m+=1
            s|=set(str(n*m))
        ans+=[''.join(['Case #',str(i),': ',str(n*m)])]
print('\n'.join(ans),file=fo)
fo.close()