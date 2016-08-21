# competition io code from https://github.com/DarioFanucchi/CompetitionCode.git
import codejam_io


N, J = map(int, codejam_io.read_straight("C-large.in")[0].split())

def num2bin(num):
    return bin(num)[2:]

begEnds = map(num2bin, range(3,J*2+3,2))

def convertNToBase(NStr, base):
        convertedNum = 0
        NStr = list(NStr)
        NStr.reverse()
        for power,digit in enumerate(NStr):
            convertedNum += int(digit)*(base**power)
        return convertedNum

def getDivisors(coinStr, m):
    divisorsStr = ""
    for base in xrange(2,11):
        divisorsStr += " " + str(convertNToBase(begEnd, base))
    return divisorsStr

answers = []
for begEnd in begEnds:
    n = len(begEnd)
    m = N - n

    numMiddle0s = N - 2*n

    coinStr = begEnd + numMiddle0s*"0" + begEnd

    answers.append(coinStr + getDivisors(coinStr, m))

answers = "\n".join(answers)

with open("C_large.out", "wt") as f:
    f.write("Case #1:\n" + answers)
