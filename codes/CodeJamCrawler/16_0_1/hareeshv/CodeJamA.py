t = input()
for i in range(t):
    n = input()
    print "Case #"+str(i+1)+": ",
    if n == 0:
        print "INSOMNIA"
        continue
    else:
        s = set();j=1
        while True:
            s.update(str(n*j))
            if len(s) == 10:
                print n*j
                break
            j += 1