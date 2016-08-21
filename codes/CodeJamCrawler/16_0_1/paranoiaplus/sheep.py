numInputs = int(raw_input())

def noSleep(digitDict):
    for i in xrange(0, 10):
        if(digitDict[str(i)] == False):
            return False
    return True

def insertDigits(digitDict, digitString):
    for char in str(digitString):
        digitDict[char] = True

def sheep(i, n):
    digitDict = { str(x): False for x in xrange(0, 10) }

    if(int(n) == 0):
        print "Case #{}: INSOMNIA".format(i)
        return

    currStr = str(n)
    x = 1
    num = n

    while(not noSleep(digitDict)):
        insertDigits(digitDict, x * int(currStr))
        num = x*n
        x += 1

    print "Case #{}: {}".format(i, num)

for i in xrange(1, numInputs + 1):
    n = int(raw_input())
    sheep(i, n)


