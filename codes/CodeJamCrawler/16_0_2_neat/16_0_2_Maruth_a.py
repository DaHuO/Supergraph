for y in range(int(input())):

    s = input()
    i = len(s) - 1
    nFlips = 0
    foo = False

    while i > -1:

        if not foo:

            while i > -1 and s[i] != '-':
                i -= 1

        else:

            while i > -1 and s[i] != '+':
                i -= 1

        if i > -1: nFlips += 1
        foo = not foo

    print("Case #%d: %d" % (y+1, nFlips))
