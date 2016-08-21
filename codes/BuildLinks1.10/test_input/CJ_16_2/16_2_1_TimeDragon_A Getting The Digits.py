#!python3

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    phoneStr = inputFile.readline()
    phoneStr = phoneStr.rstrip()
    charCount = [0] * 26
    numCount = [0] * 10

    for index in range(0, len(phoneStr)):
        charCount[ord(phoneStr[index]) - ord('A')] += 1

    numCount[0] = charCount[25]
    charCount[4] -= charCount[25]
    charCount[17] -= charCount[25]
    charCount[14] -= charCount[25]
    charCount[25] = 0

    numCount[2] = charCount[22]
    charCount[19] -= charCount[22]
    charCount[14] -= charCount[22]
    charCount[22] = 0

    numCount[4] = charCount[20]
    charCount[5] -= charCount[20]
    charCount[14] -= charCount[20]
    charCount[17] -= charCount[20]
    charCount[20] = 0

    numCount[6] = charCount[23]
    charCount[18] -= charCount[23]
    charCount[8] -= charCount[23]
    charCount[23] = 0

    numCount[8] = charCount[6]
    charCount[4] -= charCount[6]
    charCount[8] -= charCount[6]
    charCount[7] -= charCount[6]
    charCount[19] -= charCount[6]
    charCount[6] = 0

    numCount[1] = charCount[14]
    charCount[13] -= charCount[14]
    charCount[4] -= charCount[14]
    charCount[14] = 0

    numCount[3] = charCount[19]
    charCount[7] -= charCount[19]
    charCount[17] -= charCount[19]
    charCount[4] -= (2 * charCount[19])
    charCount[19] = 0

    numCount[5] = charCount[5]
    charCount[8] -= charCount[5]
    charCount[21] -= charCount[5]
    charCount[4] -= charCount[5]
    charCount[5] = 0

    numCount[7] = charCount[21]
    charCount[18] -= charCount[21]
    charCount[4] -= (2 * charCount[21])
    charCount[13] -= charCount[21]
    charCount[21] = 0

    numCount[9] = charCount[4]

    displayString = ""
    for index in range(0, 10):
        displayString += (chr(ord('0') + index) * numCount[index])

    print("Case #", testCase, ": ", displayString, sep="", file=outputFile)


inputFile.close()
outputFile.close()
