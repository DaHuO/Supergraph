def dbg(x):
    return ''.join(['+' if x_ else '-' for x_ in x])

for t in xrange(int(raw_input())):
    S = [c == '+' for c in raw_input()]
    r = len(S)-1
    flips = 0
    while r >= 0:
        if S[r]:
            r -= 1
        else:
            lf = 0
            if S[lf]:
                flips += 1
                while S[lf]:
                    S[lf] = False
                    lf += 1
            # print ">>>", dbg(S)
            S = list(map(lambda x: not x, reversed(S[:r+1])))+S[r+1:]
            flips += 1
            # print ">>>", dbg(S)
            # lf = 0
            # while lf < r and not S[lf]:
            #     print 'rev'
            #     S[lf], S[r] = not S[r], True
            #     r -= 1
            #     lf += 1
            # if lf == r:
            #     print 'flip'
            #     S[lf] = not S[lf]
    print "Case #%d: %d" % (t+1, flips)
