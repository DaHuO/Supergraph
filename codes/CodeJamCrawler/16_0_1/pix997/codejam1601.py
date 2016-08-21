t = input()
d = []
for i in range(t):
    n = [str(j) for j in range(10)]
    a = input()
    if a == 0:
        d.append("INSOMNIA")
        continue
    c =1
    f=1
    while f==1:
        f=0
        b = str(a*c)
        for j in b:
            for k in range(10):
                if j==str(k):
                    n[k]='-1'
        for j in n:
            if j!='-1':
                f=1
        if f==0:
            d.append(str(a*c))
            break
        c+=1
for i in range(t):
    print "Case #"+str(i+1)+": "+d[i]    
