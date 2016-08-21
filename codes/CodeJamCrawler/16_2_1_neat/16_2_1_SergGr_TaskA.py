import threading
import sys
from  collections import Counter
# Increase max stack size from 8MB to 512MB
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10 ** 6)

inputFileName = "test.in"
inputFileName = "A-small-attempt0.in"
# inputFileName = "A-small-attempt1.in"
# inputFileName = "A-small-attempt2.in"
# inputFileName = "A-small-attempt3.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"


# "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
#

def calcSingleTest(f):
    line = f.readline()

    d_raw = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    d_list = map(lambda x: Counter(x), d_raw)
    # [ "ONE", ,    "NINE"]
    # z=>zero
    # w=>two
    # u=>four
    # g=>eight
    # x=>"SIX"
    #########
    # s=>"SEVEN"
    # v=>"FIVE"
    # t=>"THREE"
    # o=>one
    # i => nine
    d_rev = [
        ('Z', 0),
        ('W', 2),
        ('U', 4),
        ('G', 8),
        ('X', 6),
        #########
        ('S', 7),
        ('V', 5),
        ('T', 3),
        ('O', 1),
        ('I', 9)
    ]

    s = line.translate(None, '\r\n')
    l_cnt = Counter(s)
    print l_cnt
    print d_list

    res = [''] * 10
    for (l, d) in d_rev:
        c = l_cnt[l]
        res[d] = str(d) * c
        d_l = d_list[d]
        for ad in d_l:
            l_cnt[ad] = l_cnt[ad] - c * d_l[ad]

    for k,v in l_cnt.iteritems():
        if v!= 0:
            print "!!!!!!!!!!!!!!!!"
            print l_cnt

    return ''.join(res)


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))
