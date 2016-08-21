T = input()
for t in xrange(1, T+1):
    S = raw_input()
    count = 0
    currChar = S[0]
    for c in S[1:]:
        if currChar != c:
            currChar = c
            count += 1
    if S[-1] == '-':
        count += 1
    print 'Case #%d: %d' % (t, count)
