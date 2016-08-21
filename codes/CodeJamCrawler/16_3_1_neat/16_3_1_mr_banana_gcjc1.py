t=int(input())
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for case in range(1,t+1):
    n=int(input())
    l=[int(i) for i in input().split()]
    s2=[]
    if sum(l)%2:
        x=l.index(max(l))
        s2.append(s[x])
        l[x]-=1
    while l.count(0)!=n:
        s3=''
        x=l.index(max(l))
        s3+=s[x]
        l[x]-=1
        x=l.index(max(l))
        s3+=s[x]
        l[x]-=1
        s2.append(s3)
    print('Case #%s: '%case+' '.join(s2))
