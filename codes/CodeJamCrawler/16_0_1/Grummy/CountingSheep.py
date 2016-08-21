inputFile = open("A-large.in")
outputFile = open("A-large.out", "w")

testcases = int(inputFile.readline())

for testCase in range(testcases):
    numbersSeen = []
    N = int(inputFile.readline())

    for i in range(1, 1000000):
        new = str(i * N)
        for char in new:
            if not char in numbersSeen:
                numbersSeen.append(char)

        finished = True
        for x in range(10):
            if not str(x) in numbersSeen:
                finished = False
                break

        if finished:
            print("FINAL", i * N)
            outputFile.write("Case #" + str(testCase+1) + ": " + str(i*N) + "\n")
            break

    if not finished:
        print("INSOMNIA")
        outputFile.write("Case #" + str(testCase+1) + ": INSOMNIA" + "\n")



inputFile.close()
outputFile.close()

    
    
    
    
