def solve(val):
    n = val
    nums = [False] * 10

    for k in range(1, 1000001):
        for c in str(n * k):
            if c == '1':
                nums[0] = True
            if c == '2':
                nums[1] = True
            if c == '3':
                nums[2] = True
            if c == '4':
                nums[3] = True
            if c == '5':
                nums[4] = True
            if c == '6':
                nums[5] = True
            if c == '7':
                nums[6] = True
            if c == '8':
                nums[7] = True
            if c == '9':
                nums[8] = True
            if c == '0':
                nums[9] = True
        if nums[0] and nums[1] and nums[2] and nums[3] and nums[4] and nums[5] and nums[6] and nums[7] and nums[8] and nums[9]:
            return (n * k)
            break;

    if nums[0]  == False:
        return "INSOMNIA"

fileName = str(input("File? "))

inputFile = open(fileName)
outputFile = open("A", "w")
caseCount = 1
firstLine = True
for i in inputFile.readlines():
    if (firstLine):
        firstLine = False
        continue
    outputFile.write("Case #" + str(caseCount) + ": " + str(solve(int(i))) + "\n")
    caseCount += 1
inputFile.close()
outputFile.close()
