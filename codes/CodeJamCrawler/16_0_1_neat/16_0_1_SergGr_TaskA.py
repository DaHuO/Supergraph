inputFileName = "test.in"
inputFileName = "A-small-attempt0.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"

global MY_DEBUG
MY_DEBUG = "test.in" == inputFileName

"""
def test(x0):
    digits = set()
    x = x0
    while x % 10 == 0:
        x /= 10
    for m in xrange(1, 2000):
        # t = (m * x) % 1000
        t = m * x
        d1 = t % 10
        d2 = t / 10 % 10
        d3 = t / 100 % 10
        digits.add(d1)
        digits.add(d2)
        digits.add(d3)
        digits.add(t / 1000 % 10)
        if (len(digits) == 10):
            return (True, digits, m)

    return (False, digits, -1)


mm = 0
mmx = -1
for x in xrange(1, 10000000):
    (r, d, m) = test(x)
    if m > mm:
        mm = m
        mmx = x
    if (not r):
        print "Bad " + str(x) + " " + str(d)
    if x % 10000 == 0:
        print "Progress " + str(x) + ' mm = ' + str(mm) + '  mmx = ' + str(mmx)
"""

def calcSingleTest(f):
    line = f.readline()
    x = int(line)
    if x == 0:
        return 'INSOMNIA'
    digits = set()
    # for m in xrange(1, max(1000, 10 * x)):
    for m in xrange(1, 1000): #1000 seems to be more than enough
        # t = (m * x) % 1000
        t = m * x
        while t > 0:
            d = t % 10
            t /= 10
            digits.add(d)

        if len(digits) == 10:
            return m * x
    if MY_DEBUG:
        print '!!!!Bad ' + str(x)
    return 'INSOMNIA'


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))
