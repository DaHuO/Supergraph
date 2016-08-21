t = int(raw_input())


def allNeg(a, p, q):
    for i in range(p,q+1):
        if a[i]:
            return False
    return True

for i in xrange(1,t+1):
    n = raw_input()
    p = [True if x == '+' else False for x in n]
    l = len(p)
    res = [[0 for col in xrange(l)] for row in xrange(l)]
    for h in xrange(l):
        res[h][h] = 0 if p[h] else 1
    for lens in xrange(1, l):
        for j in xrange(0, l - lens):
            tmp = 9999999999
            if (allNeg(p, j, j+lens)):
                res[j][j+lens] = 1
                continue
            for k in xrange(0, lens):
                middle = j + k
                now = 0
                if res[middle + 1][j + lens] == 0:
                    now = res[j][middle]
                else:
                    now = res[j][middle] + res[middle+1][j+lens] + 1
                if now < tmp:
                    tmp = now
            res[j][j + lens] = tmp

    print "Case #{}: {}".format(i, res[0][l-1])