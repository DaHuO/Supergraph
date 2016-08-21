import sys

def readline():
    return sys.stdin.readline().rstrip()

def gen(x, i, ans):
    if i == len(x):
        ans.append(''.join(x))
        return ans

    if x[i] != '?':
        return gen(x, i+1, ans)

    for k in '0123456789':
        x[i] = k
        gen(x, i+1, ans)
        x[i] = '?'
    return ans

def solve():
    a, b = readline().split()
    aa = gen(list(a), 0, [])
    bb = gen(list(b), 0, [])

    best = 1e100
    x, y = None, None
    for a in aa:
        for b in bb:
            diff = abs(int(a) - int(b))
            if diff < best:
                best = diff
                x, y = a, b
    print x, y
    print >>sys.stderr, x, y

if __name__ == '__main__':
    n = int(readline())
    for k in range(1, n+1):
        print 'Case #%d:' % k,
        solve()
