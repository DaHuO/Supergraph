t=int(input())
for case in range(t):
    n=int(input())
    n2=n
    l=[0,0,0,0,0,0,0,0,0,0]
    if n==0:
        n2='INSOMNIA'
    else:
        while True:
            for i in '0123456789':
                if i in str(n2)  and l[int(i)]==0:
                    l[int(i)]=1
            if l.count(1)==10:
                break
            else:
                n2+=n
    print('Case #%d: %s'%(case+1,(n2)))
                
                
