def allOne(arr):
    for n in arr:
        if (n != 1): return False
    return True

def solveSheepProb(N):
    if (N == 0): return "INSOMNIA"
    i = 1
    a = [0 for s in range(10)]
    while True:
        newNum = i*N
        numString = str(newNum)
        for s in numString:
            a[int(s)] = 1

        if (allOne(a)):
            # print "-----"
            return newNum
            # print "-----"
            break
        i += 1

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}:".format(i), solveSheepProb(n)
