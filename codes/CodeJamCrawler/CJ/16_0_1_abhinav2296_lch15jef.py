g=open("input.txt","r")
h=open("output.txt","w")
t=int(g.readline())
i=0
for line in g:
    n=int(line)
    if n==0:
        h.write('Case #%d: %s\n'%((i+1), 'INSOMNIA'))
        i+=1
        continue
    p=1
    a=[0]*10
    while True:
        k=p*n
        while k>0:
            z=k%10
            k/=10
            a[z]=1
        f=0
        for j in range(10):
            if (a[j]==0):
                f=1
                break
        if (f==0):
            break
        else:
            p+=1
    h.write('Case #%d: %d\n'%((i+1), p*n))
    i+=1
h.close()
g.close()
