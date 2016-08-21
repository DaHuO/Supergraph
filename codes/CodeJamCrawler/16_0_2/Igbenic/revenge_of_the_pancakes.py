def readWithName(filename):
    return open("../codejam/" + filename, "r+").read()


def writeToFileWithCases(filename, case, data):
    open("../codejam/" + filename, "a").write("Case #{}".format(case) + ": {}".format(data) + "\n")


input = readWithName("B-large.in.txt")
input = input.split("\n")

def flipTo(boolcakes, number):
    for i in range(number):
        boolcakes[i] = not boolcakes[i]
    return boolcakes

def getLastNotHappy(boolcakes):
    for i in range(len(boolcakes) - 1, -1, -1):
        if not boolcakes[i]:
            return i
    return -1

def toBool(pancakes):
    boolcakes = []
    for pan in pancakes:
        if pan == "+":
            boolcakes.append(True)
        else:
            boolcakes.append(False)
    return boolcakes

for i in range(1, int(input[0]) + 1):
    boolcakes = toBool(list(input[i]))

    iterations = 0
    while len(set(boolcakes)):
        unhappyPos = getLastNotHappy(boolcakes)
        if unhappyPos == -1:
            break
        boolcakes = flipTo(boolcakes, unhappyPos + 1)
        iterations += 1

    writeToFileWithCases("revenge_of_the_pancakes_solution.txt", i, iterations)