t = int(raw_input())
k=1
while t:
    n = int(raw_input())
    i = 1
    d = {}
    while True:
        f = 0
        x = n*i
        if x == 0:
            print "Case #"+str(k)+": INSOMNIA"
            break
        temp = list(str(x))
        for j in temp:
            d.setdefault(j,0)
            d[j] += 1

        for j in range(0,10):
            if str(j) not in d:
                f=1

        if f==0:
            print "Case #"+str(k)+": "+str(x)
            break
        i+=1
    k+=1
    t=t-1
