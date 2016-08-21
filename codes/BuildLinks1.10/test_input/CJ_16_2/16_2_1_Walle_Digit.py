t = int(raw_input())

for i in xrange(1, t + 1):
    s = raw_input()
    out = []
    while "Z" in s:
        out.append(0)
        s=s.replace("Z", "", 1)
        s=s.replace("E", "", 1)
        s=s.replace("R", "", 1)
        s=s.replace("O", "", 1)
    while "W" in s:
        out.append(2)
        s=s.replace("T", "", 1)
        s=s.replace("W", "", 1)
        s=s.replace("O", "", 1)

    while "G" in s:
        out.append(8)
        s=s.replace("E", "", 1)
        s=s.replace("I", "", 1)
        s=s.replace("G", "", 1)
        s=s.replace("H", "", 1)
        s=s.replace("T", "", 1)

    while "X" in s:
        out.append(6)
        s=s.replace("S", "", 1)
        s=s.replace("I", "", 1)
        s=s.replace("X", "", 1)

    while "S" in s:
        out.append(7)
        s=s.replace("S", "", 1)
        s=s.replace("E", "", 1)
        s=s.replace("V", "", 1)
        s=s.replace("E", "", 1)
        s=s.replace("N", "", 1)

    while "T" in s:
        out.append(3)
        s=s.replace("T", "", 1)
        s=s.replace("H", "", 1)
        s=s.replace("R", "", 1)
        s=s.replace("E", "", 1)
        s=s.replace("E", "", 1)

    while "R" in s:
        out.append(4)
        s=s.replace("F", "", 1)
        s=s.replace("O", "", 1)
        s=s.replace("U", "", 1)
        s=s.replace("R", "", 1)

    while "F" in s:
        out.append(5)
        s=s.replace("F", "", 1)
        s=s.replace("I", "", 1)
        s=s.replace("V", "", 1)
        s=s.replace("E", "", 1)

    while "I" in s:
        out.append(9)
        s=s.replace("N", "", 1)
        s=s.replace("I", "", 1)
        s=s.replace("N", "", 1)
        s=s.replace("E", "", 1)

    while "O" in s:
        out.append(1)
        s=s.replace("O", "", 1)
        s=s.replace("N", "", 1)
        s=s.replace("E", "", 1)
    
    out = sorted(out)
    result = ''
    for j in out:
        result += str(j)
    print "Case #{}: {}".format(i, result)

