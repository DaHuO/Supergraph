t = int(raw_input())
for i in range(1,t+1):
    x = int(raw_input())
    print "Case #"+str(i)+":",
    if x == 0:
        print "INSOMNIA"
    else:
        s = frozenset(str(x))
        n = 1
        while(len(s)!=10):
            n+=1
            s = s.union(str(n*x))
        print n*x



