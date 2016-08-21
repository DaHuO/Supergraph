T = input()
for i in xrange(T):
    S = raw_input()

    sol = S[0]
    for l in S[1:]:
        if l >= sol[0]:
            sol = l+sol
        else:
            sol = sol+l

    print 'Case #'+str(i+1)+": " + sol
