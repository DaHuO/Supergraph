#Z - 0 ZERO
#W - 2 TWO
#X - 6 SIX
#G - 8 EIGHT

#T - 3
#R - 4
#O - 1
#F - 5
#V - 7
#rest - 9

from collections import Counter

def minusOff(counter, letters, numberCount):
    for i in letters:
        counter[i] -= numberCount

T = int(input())

for caseNum in range(1, T+1):
    myLine = input().strip()
    myCounter = Counter(myLine)

    numberCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    numberCount[0] = myCounter['Z']
    numberCount[2] = myCounter['W']
    numberCount[6] = myCounter['X']
    numberCount[8] = myCounter['G']

    minusOff(myCounter, 'ZERO', numberCount[0])
    minusOff(myCounter, 'TWO', numberCount[2])
    minusOff(myCounter, 'SIX', numberCount[6])
    minusOff(myCounter, 'EIGHT', numberCount[8])

    numberCount[3] = myCounter['T']
    minusOff(myCounter, 'THREE', numberCount[3])
    numberCount[4] = myCounter['R']
    minusOff(myCounter, 'FOUR', numberCount[4])
    numberCount[1] = myCounter['O']
    minusOff(myCounter, 'ONE', numberCount[1])
    numberCount[5] = myCounter['F']
    minusOff(myCounter, 'FIVE', numberCount[5])
    numberCount[7] = myCounter['V']
    minusOff(myCounter, 'SEVEN', numberCount[7])
    numberCount[9] = myCounter['I']
    minusOff(myCounter, 'NINE', numberCount[9])


    phoneNum = []
    for num in range(len(numberCount)):
        numAppear = numberCount[num]
        for i in range(numAppear):
            phoneNum.append(num)
    phoneNumStr = ''.join(list(map(str, phoneNum)))

    print("Case #%d: %s" %(caseNum, phoneNumStr))
