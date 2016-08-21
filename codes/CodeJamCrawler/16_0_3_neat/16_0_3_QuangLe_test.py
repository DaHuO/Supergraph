def getFirstDivision(x):
    for division in xrange(2, 1000):
        if (x % division == 0):
            return division
    return -1

def isJamcoin(numStr):
    for base in xrange(2, 11):
        x = int(numStr, base)
        if (getFirstDivision(x) == -1):
            return False
    return True

n = 32;
m = 500;
for x in xrange(0, 2**30):
    numStr = "1" + "{0:b}".format(x).zfill(n-2) + "1"
    if (isJamcoin(numStr)):
        result = numStr + " "
        for base in xrange(2, 11):
            result = result + str(getFirstDivision(int(numStr, base))) + " "
        print result
        m -= 1
        if (m == 0):
            break


