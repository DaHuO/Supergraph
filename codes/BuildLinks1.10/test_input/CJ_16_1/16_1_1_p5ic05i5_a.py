
T = int(raw_input())
for x in xrange(1, T+1):
    S = raw_input()
    lw = ''
    for c in S:
        if lw == '':
            lw = c
        elif c >= lw[0]:
            lw = c + lw
        else:
            lw = lw + c
    print "Case #{}: {}".format(x, lw)
