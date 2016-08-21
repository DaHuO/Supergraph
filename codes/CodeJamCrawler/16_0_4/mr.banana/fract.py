t=int(input())
for case in range(1,t+1):
    l1=[int(i) for i in input().split()]
    k=l1[0]
    c=l1[1]
    s=' '.join([str(k**(c-1)*i) for i in range(1,k+1)])
    print('Case #%s: %s'%(case,s))
