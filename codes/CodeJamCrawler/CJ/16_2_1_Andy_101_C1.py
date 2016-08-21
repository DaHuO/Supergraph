

for ii in xrange(int(raw_input())):
    c1=raw_input()
    c=list(c1)
    c.sort()
    k=""
    while "Z" in c:
        c.remove("Z")
        c.remove("E")
        c.remove("R")
        c.remove("O")
        k=k+"0"
    while "W" in c:
        c.remove("T")
        c.remove("W")
        c.remove("O")
        k=k+"2"
    while "U" in c:
        c.remove("F")
        c.remove("O")
        c.remove("U")
        c.remove("R")
        k=k+"4"
    while "X" in c:
        c.remove("S")
        c.remove("I")
        c.remove("X")
        k=k+"6"
    while "G" in c:
        c.remove("E")
        c.remove("I")
        c.remove("G")
        c.remove("H")
        c.remove("T")
        k=k+"8"
    while "O" in c:
        c.remove("O")
        c.remove("N")
        c.remove("E")
        k=k+"1"
    while "T" in c:
        c.remove("T")
        c.remove("H")
        c.remove("R")
        c.remove("E")
        c.remove("E")
        k=k+"3"
    while "F" in c:
        c.remove("F")
        c.remove("I")
        c.remove("V")
        c.remove("E")
        k=k+"5"
    while "V" in c:
        c.remove("S")
        c.remove("E")
        c.remove("V")
        c.remove("E")
        c.remove("N")
        k=k+"7"
    while "N" in c:
        c.remove("N")
        c.remove("I")
        c.remove("N")
        c.remove("E")
        k=k+"9"
    print "Case #%d: %s"%(ii+1,''.join(sorted(k)))
