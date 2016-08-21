fileIn = open("A-large.in", "r")
fileOut = open("a_output.txt", "w")

def getDigits(num, digits):
    num = str(num)
    for i in range(len(num)):
        for j in range(len(digits)):
            if int(num[i]) == digits[j]:
                digits[j] = "x"
    return digits

caseNum = int(fileIn.readline())

for i in range(caseNum):
    line = int(fileIn.readline())
    if line == 0:
        fileOut.write("Case #" + str(i + 1) + ": INSOMNIA\n")
        continue
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    j = 0
    while digits != ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']:
        j += 1
        digits = getDigits(line * j, digits)
    fileOut.write("Case #" + str(i + 1) + ": " + str(line * j) + "\n")

fileIn.close()
fileOut.close()
