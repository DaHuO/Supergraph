import sys

nlines = int(sys.stdin.readline())
casen = 0
while 1:
    line = sys.stdin.readline()
    casen += 1
    if not line:
        break
    k, c, s = line.split()
    k = int(k)
    c = int(c)
    s = int(s)
    # print k, c, s
    if c == 1:
        if s < k:
            print 'Case #%d: IMPOSSIBLE' % (casen,)
        else:
            print 'Case #%d: %s' % (casen, ' '.join(str(i) for i in range(1,k+1)))
        continue
    if k == 1:
            print 'Case #%d: 1' % (casen,)
            continue
    if s < int((k + 1)/2):
        print 'Case #%d: IMPOSSIBLE' % (casen,)
        continue
    glen = k ** c / k
    curr_group = 1
    tocheck = []
    while curr_group <= k:
        gidx = (curr_group - 1) * glen;
        if curr_group == k:
            iidx = curr_group
        else:
            iidx = curr_group + 1
        tocheck.append(str(gidx + iidx))
        curr_group += 2
    print 'Case #%d: %s' % (casen, ' '.join(tocheck))
