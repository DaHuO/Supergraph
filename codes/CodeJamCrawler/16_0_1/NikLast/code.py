n = int(raw_input())
want = '0123456789'
for c in range(n):
    arg = int(raw_input())
    newarg = arg
    have = []
    if arg == 0:
        result = "INSOMNIA"
    else:
        while True:
            for digit in ("%d" % newarg):
                if digit not in have:
                    have.append(digit)

            if len(have)==10:
                break;
            else:
                newarg += arg

        result = "%d" % newarg

    print "Case #%d: %s" % (c+1, result)