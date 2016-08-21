import sys

f = open(sys.argv[1])

def main():
	T = int(f.readline())

    #print "Total %d" % T
	for case in xrange(1, T + 1, 1):
		doCase(case)



def doCase(case):
    #print "Case %d" % case
    S = str(f.readline().strip())
    testNum = 0

    cur = []

    # 0: '-', 1: '+'
    for pos in xrange(len(S)):
        if ('-' == S[pos]):
            cur.append(0)
        else:
            cur.append(1)

    def rmTailHappy():
        for pos in xrange(len(cur)-1, -1, -1):
            if (0 == cur[pos]):
                break

        if (0 == cur[pos]):
            pos += 1
        del cur[pos:]

    def flip (end):  
        #print "end ", end
        tmp = cur[:end+1]
        tmp.reverse()
        #print "tmp", tmp
        for pos in xrange(0, end+1, 1):
            cur[pos] = (tmp[pos] + 1) % 2
        #print "flip", cur

    def findHeadHappy():
        for pos in xrange(len(cur)):
            if (0 == cur[pos]):
                return pos - 1

        return -1

    def findHeadBlack():
        for pos in xrange(len(cur)):
            if (1 == cur[pos]):
                return pos

        return pos

    while (len(cur) > 0):
        # 1. remove tail +
        rmTailHappy()
        #print "cur ", cur
        # 2. find head +
        if (len(cur) > 0):
            pos = findHeadHappy()

            if (pos >= 0):
                flip(pos)
                testNum += 1
        
        #print "after happy", cur
        # 3. reverse all
        if (len(cur) > 0):
            flip(len(cur) - 1)
            testNum += 1
        
    print("Case #{}: {}".format(case, testNum))
    

if __name__ == '__main__':
	main()

f.close()
