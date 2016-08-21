from collections import defaultdict

def rankAndFile(matrix):
    d = defaultdict(int)
    for row in matrix:
        for n in row:
            i = int(n)
            d[i] += 1

    res = []
    for k in d:
        if d[k] % 2 == 1:
            res.append(k)
    res.sort()
    return ' '.join([str(_) for _ in res])


def solve(file):
    f = open(file, 'r')
    count = int(f.readline())
    case = 1
    for i in xrange(count):
        rowStr = f.readline()
        row = int(rowStr.strip())
        matrix = []
        for j in xrange(row*2-1):
            r = f.readline()
            matrix.append(r.split())
        print 'Case #%d: %s' % (case, rankAndFile(matrix))
        case += 1
    f.close()

solve('B-large.in')