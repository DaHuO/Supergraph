o = open('large-A.txt', 'w')

try:
    i = open('A-large.in')
except IOError:
    print('Could not find file.')

with o:
    fullList = set({0,1,2,3,4,5,6,7,8,9})
    numLines = int(i.readline())
    for k in range(numLines):
        partialList = set()
        num = int(i.readline().rstrip('\n'))
        testCase = num
        if num == 0:
            testCase = 'INSOMNIA'
        else:
            count = 1
            while not fullList.issubset(partialList):
                testCase = count * num
                for j in str(testCase):
                    if int(j) not in partialList:
                        partialList.add(int(j))
                count += 1
        o.write('Case #' + str(k+1) + ': ' + str(testCase) + '\n')
