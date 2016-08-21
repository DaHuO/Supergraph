for i in range(input()):
    print "Case #"+str(i+1)+": ",
    d = {}
    for j in range(2*input()-1):
        l = map(int, raw_input().split())
        for k in l:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
    res = []
    for (k,v) in d.items():
        if v%2 == 1:
            res.append(k)
    print ' '.join(map(str, sorted(res)))