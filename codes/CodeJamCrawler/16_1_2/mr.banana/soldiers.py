t=int(input())
for case in range(1,t+1):
    n=int(input())
    l=[]
    for i in range(2*n-1):
        l+=[int(a) for a in input().split()]
    l1=[]
    for i in l:
        if l.count(i)%2 and i not in l1:
            l1.append(i)
    s=' '.join([str(i) for i in sorted(l1)])
    print('Case #%s: %s'%(case,s))
