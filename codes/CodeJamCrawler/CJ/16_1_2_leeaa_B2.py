tn = int(raw_input())
# left is basic
# up 270
# right 180
# down 90

for ti in xrange(1, tn+1):
    N = int(raw_input())
    last = set([])
    for i in xrange(0, 2*N-1):
        tmp = map(int, raw_input().split())
        for t in tmp:
            if t in last:
                last.remove(t)
            else:
                last.add(t)
    ans = list(last)
    ans.sort()

    #print 'Case #' + str(ti) + ':'
    #for i in xrange(0, N):
    #    print ' '.join(map(str, mT[i]))
    print 'Case #' + str(ti) + ': ' + ' '.join(map(str,ans))
