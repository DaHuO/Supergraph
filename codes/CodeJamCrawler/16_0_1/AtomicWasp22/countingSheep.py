__author__ = 'Kian Jones'

f = open('A-large.in', 'r')
testCases = f.read().split('\n')
numCases = testCases[0]

testCases = testCases[1:-1]
print(testCases)
j = 0
for n in testCases:
    n = int(n)
    j += 1
    if n == 0:
        print("Case #{0}: INSOMNIA".format(j))
    else:
        digits = set()
        i = 1
        while len(digits) < 10:
            y = n * i
            lastNum = y
            yList = list(str(y))
            for num in yList:
                digits.add(int(num))
            i += 1
        print("Case #{0}: {1}".format(j, lastNum))
f.close()