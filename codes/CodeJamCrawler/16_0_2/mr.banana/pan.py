t=int(input())
d={'+':1,'-':0}
for case in range(1,t+1):
    s=input()
    l=[]
    s1=d[s[0]]
    l.append(s1)
    for i in s:
        if d[i]!=s1:
            l.append(d[i])
            s1=d[i]
    print('Case #%s: %s'%(case,(l[-1] and [len(l)-1] or [len(l)])[0]))
