#!python3


def timesFlip(pan):
    ans = 0
    pan = list(pan)
    pan = pan[:-1]

    while pan and pan[-1] == '+':
        pan = pan[:-1]

    while pan:
        if pan[0] == '-':
            ans += 1
            for i in range(0, len(pan)):
                if pan[i] == '-':
                    pan[i] = '+'
                else:
                    pan[i] = '-'
            pan.reverse()
        else:
            ans += 2
            for i in range(0, len(pan)):
                if pan[i] == '+':
                    pan[i] = '-'
                else:
                    break
            for i in range(0, len(pan)):
                if pan[i] == '-':
                    pan[i] = '+'
                else:
                    pan[i] = '-'
            pan.reverse()

        while pan and pan[-1] == '+':
            pan = pan[:-1]
    return ans

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for i in range(0, testCases):
    panStr = inputFile.readline()

    ans = timesFlip(panStr)

    print("Case #", i + 1, ": ", ans, sep="", file=outputFile)
