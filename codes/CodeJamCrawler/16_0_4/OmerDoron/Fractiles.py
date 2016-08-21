inputFileName = "C:\\Users\\t8081591\\Desktop\\D-large.in"
outputFileName = "C:\\Users\\t8081591\\Desktop\\D-large.out"

def readFileIntoList(fileName):
    with open(fileName) as f:
        content = f.readlines()
        contentFixed = [map(int, c.split()) for c in content[1:]]
        T = int(content[0])
    return (T,contentFixed)

def solveFractiles(inputList):
    (K, C, S) = (inputList[0], inputList[1], inputList[2])
    print((K,C,S))
    if (S * C < K):
        return 'IMPOSSIBLE'
    else:
        sol = ''
        nextDig = 0;
        while nextDig < K:
            nextFrac = 0
            for j in range(C):
                nextFrac += nextDig * (K**j)
                nextDig += 1
                if nextDig >= K:
                    sol += str(nextFrac + 1) + ' '
                    return sol[:len(sol)-1]
            sol += str(nextFrac + 1) + ' '
        return sol[:len(sol)-1]

def fullSolve(inFileName, outFileName):
    (T,lst) = readFileIntoList(inFileName);
    f = open(outFileName, 'w');
    for i in range(T):
        sol = solveFractiles(lst[i])
        f.write("Case #" + str(i+1) + ": " + sol + "\n")
    f.close()

fullSolve(inputFileName, outputFileName)
