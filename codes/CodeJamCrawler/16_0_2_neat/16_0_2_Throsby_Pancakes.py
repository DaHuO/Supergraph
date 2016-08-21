def flipPancakes(file):

    f = open(file)

    numCases = 0

    testCases = []

    for i, line in enumerate(f):

        if i == 0:
            numCases = int(line)

        else:

            if "-" not in str(line):
                testCases.append(0)

            elif line[0] == "-" and line[1] == "\n":
                testCases.append(1)

            elif line[2] == "\n":
                if line[0] == "+" and line[1] == "-":
                    testCases.append(2)
                if line[0] == "-" and line[1] == "-":
                    testCases.append(1)
                if line[0] == "-" and line[1] == "+":
                    testCases.append(1)

            else:
                flips = 0

                fullStack = list(line)

                while "-" in str(fullStack):

                    fullStack = checkStack(fullStack)
                    flips += 1

                testCases.append(flips)

    f.close()

    fp = open("newLarge", 'a')
    iterations = 1
    for item in testCases:
        fp.write("Case #" + str(iterations) + ": " + str(item) + "\n")
        iterations += 1

    fp.close()


def flipIt(pancakes):
    for i in range(len(pancakes)):
        if pancakes[i] == "+":
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"
    return pancakes

def checkStack(pancakes):

    topCake = pancakes[0]

    for i in range(len(pancakes)):

        if pancakes[i] == topCake:
            continue

        if pancakes[i] != topCake:
            splitStack = pancakes[:i]
            splitStack.reverse()

            flippedStack = flipIt(splitStack)

            newStack = flippedStack + pancakes[i:]
            return newStack




flipPancakes("B-large.in")