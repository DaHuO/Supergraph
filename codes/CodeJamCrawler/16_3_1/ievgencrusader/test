inputF = open('input.txt', 'r')
count = inputF.readline()

answer = ""

lettersArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
              "R", "S", "T", "U", "V",'W', "X", "Y", "Z"]

for i in range(0, int(count)):
    partiesCount = int(inputF.readline())
    initialStr = inputF.readline()
    stringsArr = initialStr.strip().split(" ")

    numbersArr = []
    numbersSum = 0
    theFirstParty = 0
    theSecondParty = 0

    for j in range(0, partiesCount):
        numbersArr.append(int(stringsArr[j]))
        numbersSum += numbersArr[j]

    globalStr = ""

    while numbersSum > 0:

        limit = 0
        for j in range(0, partiesCount):
            if numbersArr[j] > limit:
                limit = numbersArr[j]
                theFirstParty = j

        limit = 0
        for j in range(0, partiesCount):
            if limit < numbersArr[j] <= numbersArr[theFirstParty] and not j == theFirstParty:
                limit = numbersArr[j]
                theSecondParty = j

        testArr = list(numbersArr)

        testArr[theFirstParty] -= 1
        testArr[theSecondParty] -= 1
        shouldDeleteFirstMemberOnly = False
        for j in range(0, partiesCount):
            if testArr[j] > (numbersSum - 2) / 2:
                shouldDeleteFirstMemberOnly = True

        numbersArr[theFirstParty] -= 1
        string1 = "%s" % lettersArr[theFirstParty]
        numbersSum -= 1

        if not shouldDeleteFirstMemberOnly:
            numbersArr[theSecondParty] -= 1
            string1 += "%s" % lettersArr[theSecondParty]
            numbersSum -= 1

        globalStr += " %s" % string1




    answer += "Case #%d: %s\n" % (i + 1, globalStr)

outputF = open('output.txt', 'w')
outputF.write(answer)
