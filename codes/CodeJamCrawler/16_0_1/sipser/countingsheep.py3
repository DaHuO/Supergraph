def countSheep(start):
    mult = 1
    digitCount = [0]*10

    while mult<100:
        multstr = str(mult * start)
        for index in range(len(multstr)):
            if (digitCount[int(multstr[index])]==0):
                digitCount[int(multstr[index])]=1
                if (sum(digitCount))==10:
                    return str(mult * start)
        mult+=1

    return 'INSOMNIA'

def runTrials(filename):
    inputFile = open(filename)
    outputFile = open(filename.split('.')[0]+'-result.txt', 'wt')
    result = ''
    #numCases = int(input())
    numCases = int(inputFile.readline())
    for trials in range(numCases):
        #N = int(input())
        N = int(inputFile.readline())
        #result+=('Case #'+str(trials+1)+': ' + countSheep(N) + '\n')
        print('Case #'+str(trials+1)+': ' + countSheep(N), file=outputFile)
    #print(result)
    inputFile.close()
    outputFile.close()


filename = input()
runTrials(filename)




