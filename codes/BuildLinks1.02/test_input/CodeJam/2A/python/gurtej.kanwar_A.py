import sys

T = int(sys.stdin.readline())

def propCounts(counts, n):
    newcounts = {}
    tot = 0
    for i in range(n,-1,-1):
        if i in counts:
            tot += counts[i]
        if tot > 0 and i > 0:
            newcounts[i-1] = tot
    return newcounts

memo = {}

def getCounts(n):
    if n in memo:
        return memo[n]
    cs = [0,0,0]
    css = []
    cur = 0
    
    # init tree
    counts = {}
    for i in range(n+1):
        assert(i <= n)
        counts[i] = 1
    # print counts
    while counts:
        cs[cur%3] += counts[0]
        cur += 1
        css.append(counts[0])
        counts = propCounts(counts, n)
        # print counts
    assert(len(css) == n+1)
    assert(len(cs) == 3)
    memo[n] = tuple(cs)
    return memo[n]

def makeTree(top, n):
    if (n == 0):
        return top
    else:
        if (top == "P"):
            other = "R"
        elif (top == "R"):
            other = "S"
        elif (top == "S"):
            other = "P"
        else:
            assert False
        one = makeTree(top, n-1)
        two = makeTree(other, n-1)
        if (one < two):
            return one + two
        else:
            return two + one

# Cache stuff
for j in range(1,13):
    # print "getCounts",j
    getCounts(j)

for i in range(T):
    n, r, p, s = map(int, sys.stdin.readline().strip().split())
    cs = getCounts(n)
    print "Case #%d:"%(i+1),
    if (p == cs[0] and
        r == cs[1] and
        s == cs[2]):
        # Print p-top
        print makeTree("P",n)
    elif (r == cs[0] and s == cs[1] and p == cs[2]):
        # Print r-top
        print makeTree("R",n)
    elif (s == cs[0] and p == cs[1] and r == cs[2]):
        # Print s-top
        print makeTree("S",n)
    else:
        print "IMPOSSIBLE"
