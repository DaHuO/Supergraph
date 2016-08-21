
def divideN(n):
    l = list()
    while n >= 10:
        d = n % 10
        if not d in l: l.append(d)
        n = n // 10
    if not n in l: l.append(n)
    # print(l)
    return l

def calculateN(s):
    s = s + '+'
    p = None
    t = 0
    for c in s:
        if p and p != c:
            t += 1
        p = c
    return t

def main():
    numInputs = int(input())
    for i in range(numInputs):
        print("Case #%d: %d" % (i + 1, calculateN(input())))

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