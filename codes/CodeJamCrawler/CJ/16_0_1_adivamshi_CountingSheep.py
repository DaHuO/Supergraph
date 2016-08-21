def sheepCount(num,refDict,count=1):
    numDigits = list(set(list(map(int, str(num*count)))))
    for i in range(0,numDigits.__len__()):
        refDict[numDigits[i]] = True
    if cmp(refDict, [True]*10) != -1:
        return num*count
    else:
        return sheepCount(num, refDict, count+1)


def countSheep(testCase):
    for i in range(0,testCase.__len__()):
        if testCase[i] != 0:
            result = sheepCount(testCase[i],[False]*10)
            print "Case #" + str(i+1) + ": " + str(result) + "\n"
        else:
            print "Case #" + str(i+1) + ": INSOMNIA\n"

if __name__ == '__main__':
    import sys
    inputFile = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            inputFile = open(fn)
    testCount = int(inputFile.readline())
    testCase = []
    for i in range(0,testCount):
        testCase.append(int(inputFile.readline()))
    inputFile.close()
    countSheep(testCase)