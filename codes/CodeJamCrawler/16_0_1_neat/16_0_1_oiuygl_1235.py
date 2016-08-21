test = int(input())
for i in range(test):
    a = int(input())
    u = a
    if a == 0:
        print("Case #"+str(i+1)+": INSOMNIA")
    else:
        g = set()
        s = 0
        while s != 10:
            for k in str(a):
                if k not in g:
                    g.add(k)
                    s+=1
            if s == 10:
                break
            a +=u
        print("Case #"+str(i+1)+": "+str(a))
            
    
