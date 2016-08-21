__author__ = 'rutger'

problemName = "problem.txt"
f = open(problemName, 'w')

def toNumber(s):
    if s == "ZERO":
        return "0"
    if s == "ONE":
        return "1"
    if s == "TWO":
        return "2"
    if s == "THREE":
        return "3"
    if s == "FOUR":
        return "4"
    if s == "FIVE":
        return "5"
    if s == "SIX":
        return "6"
    if s == "SEVEN":
        return "7"
    if s == "EIGHT":
        return "8"
    if s == "NINE":
        return "9"


def solve(number, dig):

    emptyDig = True
    for e in "ZERONTWHFUIVSXG":
        if dig.get(e, -1) > 0:
            emptyDig = False
    if emptyDig:
        return True, sorted(number)

    found = False
    for digit in ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]:
        foundDigit = True
        for character in digit:
            a = dig.get(character, -1)
            if a == -1 or a == 0:
                foundDigit = False

        if foundDigit:
            found = True
            dig2 = dig.copy()
            number2 = number + toNumber(digit)
            for character in digit:
                dig2[character] -= 1
            solved, result = solve(number2, dig2)
            if solved:
                return True, sorted(result)
    if not found:
        return False, {}
    return False, {}



T = int(input())
for t in range(T):
    # do input
    s = input()

    dig = {}
    for d in s:
        a = dig.get(d, -1)
        if a == -1:
            dig[d] = 1
        else:
            dig[d] = a + 1

    # solve input
    solved, result = solve("", dig)
    res = ""
    for e in result:
        res += e

    # print result
    f.write("Case #%d: %s\n" % (t+1, res))



f.close()