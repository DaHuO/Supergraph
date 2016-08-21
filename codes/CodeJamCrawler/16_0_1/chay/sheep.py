def fun(n):
    tmp=[0 for i in range(10)]
    for i in range(1,200):
        m=int(n*i)
        while m>0:
            tmp[int(m%10)]=1
            m=int(m/10)
        if len([j for j in tmp if j==1])==10:
            return n*i
    return 'INSOMNIA'

T=int(input())
for t in range(T):
    n=int(input())
    print('Case #{0}: {1}'.format(t+1,fun(n)))
