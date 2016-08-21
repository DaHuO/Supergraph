n=input()
a=[]
for i in range (n):
    
    a.append(int(input()))
for r in range(len(a)):
    j=1
    d=[]
    c=[]
    

    while j>0:
        k=a[r]*j
        t=k
        while k>0:
            y=k%10
            c.append(y)
            k=k//10
        for i in range(len(c)):
            if c[i] not in d:
                d.append(c[i])
    
        j=j+1
        if len(d)==10:
            print "Case #" + str(r+1) + ': '+str(t)
            break
        if t==0:
            print "Case #" + str(r+1) + ': INSOMNIA'
            break
