def readWithName(filename):
    return open("../codejam/" + filename, "r+").read()

def writeToFileWithCases(filename, case, data):
    open("../codejam/" + filename, "a").write("Case #{}".format(case) + ": {}".format(data) + "\n")

input = readWithName("A-large.in.txt")
input = input.split("\n")

gotDigits = [
    False,  # 0
    False,  # 1
    False,  # ...
    False,
    False,
    False,
    False,
    False,
    False,
    False
]

case = 1
allTrue = True

for i in range(1, int(input[0]) + 1):
    if int(input[i]) == 0:
        writeToFileWithCases("counting_sheep.txt", case, "INSOMNIA")
        case += 1
        continue
    currentMultiplier = 1
    while True:
        currentNumber = int(input[i]) * currentMultiplier
        for integer in range(0, 10):
            if str(integer) in str(currentNumber):
                gotDigits[integer] = True
                allTrue = True
                for digit in gotDigits:
                    if not digit:
                        allTrue = False
                if allTrue:
                    writeToFileWithCases("counting_sheep.txt", case, currentNumber)
                    case += 1
                    break
        currentMultiplier += 1
        if allTrue:
            gotDigits = [
                False,  # 0
                False,  # 1
                False,  # ...
                False,
                False,
                False,
                False,
                False,
                False,
                False
            ]
            break
