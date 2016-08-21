fOut = open('A-large.out', 'w')
with open('A-large.in', 'r') as f:
    testCases = int(f.readline().strip('\n'))
    
    for i in range(testCases):
        n = f.readline().strip('\n')
        nInt = int(n)
        origInt = nInt
        numbersSeen = [False for w in range(10)]
        for k in range(10000):
            n = str(nInt)
            for number in n:
                numbersSeen[int(number)] = True
            nInt += origInt
            if all(numbersSeen):
                break

        if all(numbersSeen):
            fOut.write("Case #" + str(i+1) + ": " + n + '\n')
            print ("Case #" + str(i+1) + ": " + n)
        else:
            fOut.write("Case #" + str(i+1) + ": " + "INSOMNIA" + '\n')
            print ("Case #" + str(i+1) + ": " + "INSOMNIA")
fOut.close()
