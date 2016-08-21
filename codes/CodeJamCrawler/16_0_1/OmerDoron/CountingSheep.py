inputFileName = "C:\\Users\\t8081591\\Desktop\\A-large.in"
outputFileName = "C:\\Users\\t8081591\\Desktop\\A-large.out"

def readFileIntoList(fileName):
    with open(fileName) as f:
        content = f.readlines()
        contentFixed = [map(int, c.split()) for c in content[1:]]
        T = int(content[0])
    return (T,contentFixed)

def solveCountingSheep(inputList):
    num = inputList[0]
    if num == 0:
        return 'INSOMNIA'
    else:
        times = 0;
        seen = set()
        while len(seen) < 10:
            times += 1
            for c in str(times * num):
                if int(c) not in seen:
                    seen.add(int(c))
        return str(times * num)

def fullSolve(inFileName, outFileName):
    (T,lst) = readFileIntoList(inFileName);
    f = open(outFileName, 'w');
    for i in range(T):
        sol = solveCountingSheep(lst[i])
        f.write("Case #" + str(i+1) + ": " + sol + "\n")
    f.close()

fullSolve(inputFileName, outputFileName)
