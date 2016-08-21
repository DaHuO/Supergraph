n = input()
n = int(n)
ans = [] 
for i in range(0,n):
    a = input()
    a = int(a)
    c = [10,10,10,10,10,10,10,10,10,10]
    p = 0
    e = 0
    g = a
    while(True):
        if a == 0:
            ans.append("INSOMNIA")
            break
        w = g
        p = 0
        while(int(w) != 0):
            b = w % 10
            c[b] = b
            w = int(w / 10)
        for i in range(0,10):
            if c[i] != 10:
                p += 1
        if p == 10:
            ans.append(g)
            break
        e += 1
        g = a * e
for i in range(0,len(ans)):
    print "Case #"+str(i+1)+":"+" "+ str(ans[i])
















            
    
