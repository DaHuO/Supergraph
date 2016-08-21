def solution(s):
    listOfNumbers =["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    answerList = []
    if "Z" in s:
        while "Z" in s:
            s = removeLetter(s, listOfNumbers[0])
            answerList.append("0")

    if "W" in s:
        while "W" in s:
            s = removeLetter(s, listOfNumbers[2])
            answerList.append("2")

    if "U" in s:
        while "U" in s:
            s = removeLetter(s, listOfNumbers[4])
            answerList.append("4")

    if "G" in s:
        while "G" in s:
            s = removeLetter(s, listOfNumbers[8])
            answerList.append("8")

    if "H" in s:
        while "H" in s:
            s = removeLetter(s, listOfNumbers[3])
            answerList.append("3")

    if "F" in s:
        while "F" in s:
            s = removeLetter(s, listOfNumbers[5])
            answerList.append("5")

    if "X" in s:
        while "X" in s:
            s = removeLetter(s, listOfNumbers[6])
            answerList.append("6")

    if "V" in s:
        while "V" in s:
            s = removeLetter(s, listOfNumbers[7])
            answerList.append("7")

    if "I" in s:
        while "I" in s:
            s = removeLetter(s, listOfNumbers[9])
            answerList.append("9")

    if "O" in s:
        while "O" in s:
            s = removeLetter(s, listOfNumbers[1])
            answerList.append("1")

    answerList.sort(key=int)

    answer = ""
    for i in range(0, len(answerList)):
        answer += answerList[i]

    return answer





def removeLetter(s, numberFromList):
    for letter in numberFromList:
        s = s.replace (letter, "", 1)
        # print s
    return s


def main():
    outputFile = open("output.txt", "w")
    inputFile = open("input.in")

    line =inputFile.read().splitlines()
    for i in range(1, len(line)):
        answer = solution(line[i])
        outputFile.write("Case #" + str(i) + ": " + answer + "\n")

    outputFile.close()
    inputFile.close()

main()
