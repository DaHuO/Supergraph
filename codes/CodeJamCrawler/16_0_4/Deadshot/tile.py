with open("input.txt","r+") as f:
    w = open("output.txt","w")
    n = int(f.readline())
    for a0 in range(1,n+1):
        s = f.readline()
        k,c,s = map(int,s.split(' '))
        l = []
        vark = k
        print k,c,s
        if k == 1:
            l = [1]
        elif c == 1:
            for i in range(1,k+1):
                l.append(i)
        else:
            if k%2 == 1:
                #l.append(k)
                vark -= -1
                #k-=1
            if s<k/2:
                print "IMPOSSIBLE"
            else:
                x = 2
                res = 0
                for i in range(1,vark/2+1):
                    if(res+x <= k**c):
                        l.append(res+x)
                    elif(res <= k**c):
                        l.append(k)
                    x += 2
                    res += (k**(c-1))*2
        s = "Case #%d: "%a0
        w.write(s)
        for i in range(0,len(l)):
            s = str(l[i])
            w.write(s+" ")
            print s,
        print ""
        w.write("\n")
w.close()
'''i = 1
            x = 2
            r = 0
            while(r+x<=k**c):
                l.append(r+x)
                r = (k**(c-1))*i
                print "--------",r
                i+=2
                x+=2
        print l'''
