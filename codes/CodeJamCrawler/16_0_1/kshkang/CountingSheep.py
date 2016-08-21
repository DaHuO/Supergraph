
# Number Given

# Check if N has digits in 0-9

# Check same for every N * 2,3,4,5,6,....

# When every digit has been seen, post the last number seen

# If it goes on forever Number is Insomnia


file = open("A-large.in")
answer = open("answer.txt", "r+")

numOfCases = int(file.readline().strip("\n"));

# Get test number
def getNum(file):
    return int(file.readline().strip("\n"))

# Test number
def testNum(num,checkList):
    strNum = str(num)
    for x in range(len(strNum)):
        if int(strNum[x]) in checkList:
            checkList.remove(int(strNum[x]))
    return checkList

for case in range(numOfCases):
    num = getNum(file)
    checkList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    checkList = testNum(num,checkList)
    mult = 2
    while len(checkList) > 0:
        newNum = num * mult
        mult = mult + 1
        checkList = testNum(newNum, checkList)
        print(newNum)
        if newNum > 10000000000000 or newNum == 0:
            newNum = "INSOMNIA"
            break
    answer.write(("Case #%s: %s%s") % (case + 1, newNum,"\n"))


answer.close()
file.close()




