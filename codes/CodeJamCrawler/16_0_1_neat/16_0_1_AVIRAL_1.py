from sys import stdin as sin
 
t = int(sin.readline())
for k in range(1,t+1):
    n = int(sin.readline())
    if n==0:
        print("Case #%d: INSOMNIA"%(k))
    else:
        a=[0]*10
        j=1
        while 0 in a:
            m=str(n*j)
            for i in range(len(m)):
            	r = int(m[i])
            	a[r] = 1
            j=j+1
        print('Case #%d: %d'%(k,(j-1)*n))