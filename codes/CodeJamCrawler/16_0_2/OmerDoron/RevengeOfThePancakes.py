inputFileName = "C:\\Users\\t8081591\\Desktop\\B-large.in"
outputFileName = "C:\\Users\\t8081591\\Desktop\\B-large.out"

def readFileIntoList(fileName):
    with open(fileName) as f:
        content = f.readlines()
        contentFixed = [c.split() for c in content[1:]]
        T = int(content[0])
    return (T,contentFixed)

def solveRevengeOfThePancakes(inputList):
    if (len(inputList) == 0):
        return 0
    str0 = inputList[0]
    if str0 == '+' * len(str0):
        return 0
    if str0[len(str0) - 1] == '+':
        return solveRevengeOfThePancakes([str0[:len(str0)-1]])
    if str0[0] == '-':
        stillMinus = True
        newString = ''
        for c in str0:
            if stillMinus:
                if c == '+':
                    stillMinus = False
            if not stillMinus:
                if c == '-':
                    newString = '+' + newString
                else:
                    newString = '-' + newString
        return solveRevengeOfThePancakes([newString]) + 1
    if str0[0] == '+':
        count = 0
        for c in str0:
            if c == '+':
                count += 1
            if c == '-':
                break
        newString = '-' * count + str0[count:]
        return solveRevengeOfThePancakes([newString]) + 1


def fullSolve(inFileName, outFileName):
    (T,lst) = readFileIntoList(inFileName);
    f = open(outFileName, 'w');
    for i in range(T):
        sol = solveRevengeOfThePancakes(lst[i])
        f.write("Case #" + str(i+1) + ": " + str(sol) + "\n")
    f.close()

fullSolve(inputFileName, outputFileName)
