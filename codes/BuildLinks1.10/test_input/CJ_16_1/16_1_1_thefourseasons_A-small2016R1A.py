with open("A-large2016R1A.in") as z:
    a = z.readline()
    for b in range (0, int(a)):
        c = z.readline()
        d = []
        highest = 0
        for e in range (0, len(c)):
            d.append(ord(c[e]))
        for f in range (0, len(d)):
            if d[f]>=highest:
                highest = d[f]
                c = c[f] + c[:f] + c[f+1:]
                d = []
                for e in range (0, len(c)):
                    d.append(ord(c[e]))
            else:
                pass
        print("Case #" + str(b+1) + ": " + str(c))
