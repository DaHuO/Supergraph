from collections import defaultdict

T = int(raw_input().strip())


def checkGridRule(frontS, backS):
    L = len(frontS)

    for i in xrange(L):
        s1 = frontS[i]
        s2 = backS[i]

        if s1 >= s2:
            return False

    return True


def analyzeGrid(g):
    cnt = defaultdict(int)
    hset = set()
    for l in g:
        for h in l:
            cnt[h] += 1
            hset.add(h)

    return [hset, cnt]


for i in xrange(T):
    N = int(raw_input().strip())
    lines = sorted(
        [raw_input().strip() for j in xrange(2 * N - 1)],
        key=lambda x: int(x.split(' ')[0])
    )

    cnt = defaultdict(int)
    for l in lines:
        for h in l.split(' '):
            cnt[h] += 1

    missingList = []
    for h, c in cnt.iteritems():
        if c % 2 == 1:
            missingList.append(int(h))

    missingList = sorted(missingList)
    assert len(missingList) == N

    print 'Case #%d: %s' % (
        i + 1,
        ' '.join([str(h) for h in missingList])
    )
