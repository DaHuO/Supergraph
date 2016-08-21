def genb10Div(num, p, tp, resArr, count, pows):
    if len(resArr) == count:
        return
    if p == tp:
        resArr.append(num + pows[p])
        return

    if p % 2:
        genb10Div(num, p+1, tp, resArr, count, pows)
    else:
        for i in range(2):
            genb10Div(num + pows[p] * i, p+1, tp, resArr, count, pows)

def genPows(n):
    pows = [[0 for x in range(0, n)] for x in range(11)]
    for i in range(2, 11):
        tmp = 1
        for j in range(0, n):
            pows[i][j] = tmp
            tmp = tmp * i
    return pows

def computeBNum(pre, pows):
    p = 0
    res = 0
    while pre != 0:
        rem = int(pre % 10)
        res = res + rem * pows[p]
        pre = int(pre / 10)
        p   = p + 1

    return res


t = int(raw_input())
for i in xrange(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]

    pows = genPows(n)
    b10Divs = []
    genb10Div(1, 1, n-2, b10Divs, j, pows[10])

    print "Case #1:"
    for i in range(j):
        outStr = ""
        outStr = outStr + str(11 * b10Divs[i])
        for j in range(2, 10):
            outStr = outStr + " " + str(computeBNum(b10Divs[i], pows[j]))
        outStr = outStr + " " + str(b10Divs[i])
        print outStr
