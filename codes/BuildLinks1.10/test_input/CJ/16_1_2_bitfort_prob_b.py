

T = raw_input()


def intersect(row, posn, cols, skip=None):
    cs = []
    covered = set([i for i in xrange(len(row))])
    for ci, c in enumerate(cols):
        if skip is not None and skip == ci:
            continue
        for i in xrange(len(row)):
            if row[i] == c[posn]:
                cs.append( (i, c) )
                if i in covered:
                    covered.remove(i)
                break
    return covered, cs


def solve(l):
    N = (len(l) + 1) / 2


    diag = [set([p[i] for p in l]) for i in xrange(N)]

    smallest = min([p[0] for p in l])
    biggest = max([p[-1] for p in l])

    levels = []
    has_one = None
    for i in xrange(N):
        smallest = min([p[i] for p in l])
        zeros = filter(lambda p: p[i] == smallest, l)
        for z in zeros:
            l.remove(z)
        if len(zeros) == 1:
            has_one = i
        levels.append(zeros)

    compli = levels[has_one][0]
    ans = []
    for i in xrange(N):
        if i == has_one:
            ans.append(compli[i])
            continue
        if levels[i][0][has_one] != compli[i]:
            ans.append(levels[i][0][has_one])
        else:
            ans.append(levels[i][1][has_one])
    return ans



for t in xrange(int(T)):
    N = int(raw_input())
    l = []
    for n in xrange(N * 2 - 1):
        l.append(map(int, raw_input().split()))
    ans = solve(l)
    print 'Case #{}: {}'.format(t+1, ' '.join(map(str, ans)))
