myInput = open('A-large.in', 'r')
myOutput = open('outputLarge.txt', 'w')

T = myInput.readline();
case = 0
for N in myInput:
    case += 1
    if N[0] == '0':
        myOutput.write('Case #%d: INSOMNIA\n' % (case))
    else:
        mySet = set()
        ans = 0
        while len(mySet) < 10:
            ans += 1
            intN = int(N) * ans
            strN = str(intN)
            for i in range(len(strN)):
                if strN[i] not in mySet:
                    mySet.add(strN[i])
        myOutput.write('Case #%d: %d\n' % (case, intN))


myInput.close()
myOutput.close()
