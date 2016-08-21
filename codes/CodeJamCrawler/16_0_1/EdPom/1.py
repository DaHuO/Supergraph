
def divideN(n):
    l = list()
    while n >= 10:
        d = n % 10
        if not d in l: l.append(d)
        n = n // 10
    if not n in l: l.append(n)
    # print(l)
    return l

def calculateN(n):
    UPPER_LIMIT = 100
    checkList = [False] * 10
    i = 1
    while i < UPPER_LIMIT:
        N = n * i
        for j in divideN(N): checkList[j] = True
        if all(checkList):
            return N
        else:
            i += 1
    return -1

def main():
    numInputs = int(input())
    for i in range(numInputs):
        o = calculateN(int(input()))
        if o == -1:
            print("Case #%d: INSOMNIA" % (i + 1))
        else:
            print("Case #%d: %d" % (i + 1, o))

def testSmallDataSet():
    for i in range(200):
        print("Case #%d: %d" % (i, calculateN(i)))

def testLargeDataSet():
    for i in range(10 ** 6 - 200, 10 ** 6):
        print("Case #%d: %d" % (i, calculateN(i)))

if __name__ == '__main__':
    import sys
    if '-d' in sys.argv:
        testSmallDataSet()
    elif '-db' in sys.argv:
        testLargeDataSet()
    else:
        main()