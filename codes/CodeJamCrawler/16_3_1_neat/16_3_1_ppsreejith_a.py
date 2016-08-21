def valid():
    maxi = 0
    maxc = 'A'
    sumi = 0
    for c in sens:
        if sens[c] > maxi:
            maxi = sens[c]
            maxc = c
        sumi += sens[c]
    if 2*maxi > sumi:
        return None, None
    if sumi == 0:
        return None, 'A'
    smaxi = 0
    maxc2 = 'B'
    for c in sens:
        if sens[c] > smaxi:
            if c == maxc:
                continue
            smaxi = sens[c]
            maxc2 = c
    return maxc, maxc2

path = []

def solve():
    global path
    a, b = valid()
    if a is None and b is not None:
        return True
    if a is None and b is None:
        return False
    sens[a] -= 2
    path.append(a*2)
    if solve():
        return True
    path.pop()
    sens[a] += 1
    sens[b] -= 1
    path.append(a+b)
    if solve():
        return True
    path.pop()
    sens[b] += 1
    path.append(a)
    if solve():
        return True
    return False

T = int(input())
sens = {}
for _ in xrange(T):
    path = []
    N = int(input())
    arr = map(int, raw_input().split())
    sens = {}
    for ind, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if ind >= len(arr):
            break
        sens[c] = arr[ind]
    solve()
    print "Case #%d: %s" % (_+1, " ".join(path))
