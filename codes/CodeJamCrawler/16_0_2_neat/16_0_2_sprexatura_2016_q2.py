f = open('input.large', 'r')
o = open('large.out', 'w')
T = int(f.readline().strip())

def flipWhile(N, toIdx):
    cakes = N[:]
    for idx in range(toIdx+1):
        if cakes[idx]  == '-':
            cakes[idx] = '+'
        else:
            cakes[idx] = '-'
    return cakes

def getFlipIdx(N):
    cakes = N[:]
    l = len(cakes)
    cnt = 0
    flipIdx = -1 # mean no more
    for idx in xrange(0, l):
        if cakes[idx] == '-':
            if idx == l-1: # is last?
                flipIdx = idx
                break
            if cakes[idx+1] == '+':
                flipIdx = idx
                break
    return flipIdx
            

def solve(N):
    flipIdx = getFlipIdx(N)
    cakes = N[:]
    flipCnt = 0
    while flipIdx != -1:
        cakes = flipWhile(cakes, flipIdx)
        flipCnt = flipCnt + 1
        flipIdx = getFlipIdx(cakes)
    return flipCnt

for t in xrange(T):
    n = f.readline().strip()
    n = list(n)
    res = solve(n)
    s = "Case #%d: %s\n" % (t+1, res)
    #print s
    o.write(s)

