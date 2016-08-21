# run with PyPy 2.6.1

def read_ints(line):
    return [int(x) for x in line.strip().split(' ')]


def read_floats(line):
    return [float(x) for x in line.strip().split(' ')]

def tieProb(a, p):
    p = [p[i] for i in a]
    k = len(a)
    cur = [0] * (k + 1)
    cur[0] = 1
    for i in xrange(k):
        nxt = [0] * (k + 1)
        for j in xrange(k):
            nxt[j] += cur[j] * (1 - p[i])
            nxt[j + 1] += cur[j] * p[i]
        cur = nxt
    return cur[k / 2]

def f(n, k, p):
    p.sort()
    ans = -1
    bestA = None
    for mask in xrange(2**n):
        t = mask
        a = []
        for i in xrange(n):
            if t % 2:
                a.append(i)
            t /= 2
        if len(a) != k:
            continue
        x = tieProb(a, p)
        if x > ans:
            ans = x
            bestA = a
    # print bestA
    return ans

def g(n, k, p):
    p.sort()
    ans = -1
    bestA = None
    for left in xrange(k + 1):
        right = k - left
        a = range(left) + range(n - right, n)
        x = tieProb(a, p)
        if x > ans:
            ans = x
            bestA = a
    # print bestA
    return ans

test_count = int(raw_input().strip())
for test in xrange(1, test_count + 1):
    n, k = read_ints(raw_input())
    p = read_floats(raw_input())
    print 'Case #{}: {:.10f}'.format(test, g(n, k, p))