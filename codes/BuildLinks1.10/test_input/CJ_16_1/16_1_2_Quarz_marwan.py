def readInt(): return int(raw_input())
def readList(): return map(int, raw_input().split(' '))

t = readInt()
global vis, g
global result
def check(g, a):

    for i in g:
        for j in xrange(1, len(i)):
            if i[j] <= i[j-1]:
                return False

    for i in zip(*g):
        for j in xrange(1, len(i)):
            if i[j] <= i[j-1]:
                return False
    return True

def solve(k, n, a):
    global g
    global vis
    if k == n:
        if check(g, a[:]):
            for i in a:
                if a.count(i) > (g.count(i) + (map(list, zip(*g))).count(i)):
                    return
            global result
            result = g[:]
        return

    for i in xrange(2*n-1):
        if vis[i] == 1:
            continue
        g.append(a[i])
        vis[i] = 1
        if check(g, a[:]):
            solve(k+1, n, a)
        g.pop()
        vis[i] = 0

for l in xrange(t):
    n = readInt()
    a = []
    for i in xrange(2*n-1):
        a.append(readList())
    global g
    global vis
    g = []
    vis = [0] * (2*n-1)
    solve(0, n, a)

    print "Case #" + str(l+1) + ":",
    for i in result:
        for j in range(len(a)):
            if a[j] == i:
                a.pop(j)
                break
    for i in map(list, zip(*result)):
        if not i in a:
            for k in i:
                print k,
            break

    print