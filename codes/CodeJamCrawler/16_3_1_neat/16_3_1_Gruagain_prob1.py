import string


def main():
    file = open('A-large.in', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToIntList(file.readline())
        senators = lineToIntList(file.readline())
        print(line)
        print(senators)
        answer = solve(line, senators)
        output = "Case #" + str(x + 1) + ": " + str(answer)
        print(output)
        fileOut.write(output + '\n')
    file.close()
    fileOut.close()


def solve(line, senators):
    num2alpha = dict(zip(range(0, 26), string.ascii_uppercase))
    ans = ''
    total = getTotal(senators)
    print(total)
    majority = getMajority(total)
    while total > 0:
        largestParty = findLargest(senators)
        print(largestParty)
        if senators.count(senators[largestParty]) == 2:
            print('1')
            countOfSenators = senators[largestParty]
            tempindex = -1
            for x in range(len(senators)):
                print(tempindex)
                if senators[x] == countOfSenators and tempindex == -1:
                    print('x =', x)
                    senators[x] = senators[x] - 1
                    tempindex = x
                    print(tempindex)
                elif senators[x] == countOfSenators:
                    print('y =', x)
                    senators[x] = senators[x] - 1
                    ans = ans + \
                        str(num2alpha[tempindex]) + str(num2alpha[x]) + ' '
                    break
        elif senators.count(senators[largestParty]) == 1:
            print('2')
            if senators[largestParty] > 1:
                senators[largestParty] = senators[largestParty] - 2
                ans = ans + \
                    str(num2alpha[largestParty]) + \
                    str(num2alpha[largestParty]) + ' '
            else:
                senators[largestParty] = senators[largestParty] - 1
                ans = ans + str(num2alpha[largestParty]) + ' '
        else:
            print('3')
            senators[largestParty] = senators[largestParty] - 1
            ans = ans + str(num2alpha[largestParty]) + ' '
        total = getTotal(senators)
    return ans


def findLargest(senators):
    largestParty = 0
    for x in senators:
        if x > senators[largestParty]:
            largestParty = senators.index(x)
    return largestParty


def getMajority(total):
    return total / 2 + 1


def getTotal(senators):
    total = 0
    for x in senators:
        total = total + x
    return total


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
