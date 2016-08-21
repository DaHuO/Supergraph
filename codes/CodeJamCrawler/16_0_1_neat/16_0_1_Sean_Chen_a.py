import sys

f = open(sys.argv[1])

def main():
	T = int(f.readline())

    #print "Total %d" % T
	for case in xrange(1, T + 1, 1):
		result = doCase(case)
        #print("Case #{}: {}\n".format(case, 'INSOMNIA' if (result == 0) else result))



def doCase(case):
    #print "Case %d" % case
    N = int(f.readline())
    testNum = 1
    #print "N %d" % N
    if (0 == N):
        print("Case #{}: {}".format(case, 'INSOMNIA'))
        return 0

    digiList = []
    unDigi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Npos = len(str(N))
    #print "Npos %d" % Npos

    i = N
    for pos in xrange(Npos):
        j = i % 10
        #print "j %d" % j
        digiList.insert(pos, j)

        if j in unDigi:
            unDigi.remove(j)

        i = i / 10


    #print "digi list", digiList
    #print "un digi", unDigi

    curList = list(digiList)

    def digiAdd (pos, val):
        if pos >= len(curList):
            curList.insert(pos, 0)

        i = curList[pos] + val
        if (i >= 10):
            curList[pos] = i % 10

            carry = i / 10
            digiAdd(pos+1, carry)
        else:
            curList[pos] = i


    while (len(unDigi) > 0):
        testNum += 1
        #print "Test %d" % testNum

        for pos in xrange(Npos):
            digiAdd(pos, digiList[pos])
        #print "cur", curList

        for i in xrange(len(curList)):
            j = curList[i]
            if j in unDigi:
                unDigi.remove(j)
                #print "undigi", unDigi
                if len(unDigi) == 0:
                    num = 0
                    for pos in xrange(len(curList)):
                        num += curList[pos] * (10 ** pos)
                    print("Case #{}: {}".format(case, num))
                    return testNum


if __name__ == '__main__':
	main()

f.close()