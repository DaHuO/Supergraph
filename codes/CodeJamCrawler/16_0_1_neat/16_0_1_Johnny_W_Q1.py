def solve(n):
    if n == 0:
        return 'INSOMNIA'
    checkTable = [False] * 10
    f = 1
    while True:
        lastNum = n * f
        numList = map(int,list(str(lastNum)))
        for num in numList:
            checkTable[num] = True
        if reduce(lambda x,y:x and y, checkTable) == True:
            return lastNum
        else:
            f += 1

T = input()
for c in xrange(1, T + 1):
    N = input()
    # print N
    res = solve(N)
    print "Case #%d: %s"% (c, res)