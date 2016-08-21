
d = {}
d[(1,'rp')] = (1, 1, 0)
d[(1,'ps')] = (0, 1, 1)
d[(1,'sr')] = (1, 0, 1)
for n in range(2, 13):
    for idx in range(n):
        d[(n, 'rp')] = (d[(n-1, 'rp')][0]+d[(n-1, 'rp')][1], d[(n-1, 'rp')][1]+d[(n-1, 'rp')][2], d[(n-1, 'rp')][0]+d[(n-1, 'rp')][2])
        d[(n, 'ps')] = (d[(n-1, 'ps')][0]+d[(n-1, 'ps')][1], d[(n-1, 'ps')][1]+d[(n-1, 'ps')][2], d[(n-1, 'ps')][0]+d[(n-1, 'ps')][2])
        d[(n, 'sr')] = (d[(n-1, 'sr')][0]+d[(n-1, 'sr')][1], d[(n-1, 'sr')][1]+d[(n-1, 'sr')][2], d[(n-1, 'sr')][0]+d[(n-1, 'sr')][2])

fp = open("b1s.txt")
fw = open("b1a.txt", 'w')
t = int(fp.readline().strip())
 
for case in range(t):
    n, r, p, s = fp.readline().strip().split()
    start = ''
    n = int(n)
    r = int(r)
    p = int(p)
    s = int(s)
    for init in ['rp', 'ps', 'sr']:
        print(init, (r, p, s), d[(n, init)])
        if (r, p, s) == d[(n, init)]:
            start = init
    if not start:
        fw.write("Case #{0}: {1}\n".format(case+1, 'IMPOSSIBLE'))
    else:
        if start == 'rp':
            start = 'pr'
        if start == 'ps':
            start = 'ps'
        if start == 'sr':
            start = 'rs'
        #print(start)
        for idx in range(n-1):
            end = ''
            for c in start:
                if c == 'r':
                    end += 'rs'
                if c == 'p':
                    end += 'pr'
                if c == 's':
                    end += 'ps'
            start = end
        z = [start[i]+start[i+1] for i in range(0,len(start),2)]
        for _ in range(n-1):
            s = []
            for i in range(0,len(z),2):
                if z[i] > z[i+1]:
                    s.append(z[i+1]+z[i])
                else:
                    s.append(z[i]+z[i+1])
            z = s
            print(len(z))
        fw.write("Case #{0}: {1}\n".format(case+1, z[0]))
    
    
#    fw.write("Case #{0}: {1}\n".format(case+1, g))

    
