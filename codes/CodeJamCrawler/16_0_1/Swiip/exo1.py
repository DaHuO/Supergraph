def getLastNumber(strNumber):
    if strNumber == "0":
        return "INSOMNIA"
    else:
        remainingNumbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        N = 1
        currentNbr = int(strNumber)
        while (len(remainingNumbers) is not 0):
            nbr = N * int(strNumber)
            nbr = str(nbr)
            for i in range(len(nbr)):
                current = {int(nbr[i])}
                remainingNumbers = remainingNumbers -  current
            currentNbr = int(nbr)
            N = N+1
        return str(nbr)
            


def exo1(inputPath):
    f = open(inputPath, 'r')
    f.readline()
    i = 1
    for line in f:
        print("Case #" + str(i) + ": " + getLastNumber(line.rstrip()))
        i = i+1
    f.close()



if __name__ == "__main__":
    exo1("LargeInput.in")
