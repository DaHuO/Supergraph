t=int(input())
c=1
while t!=0:
    f=0;i=2
    m=set()
    p={'0','1','2','3','4','5','6','7','8','9'}
    n=int(input())
    k=n
    if n==0:
        print("Case #"+str(c)+": INSOMNIA")
    else:
        while(f==0):
            l=list(str(k))
            m |= set(l)
            #print(m,p)
            k=n*i
            i+=1
            if m == p:
                f=1
                print("Case #"+str(c)+":",k-n)
    c+=1
    t-=1