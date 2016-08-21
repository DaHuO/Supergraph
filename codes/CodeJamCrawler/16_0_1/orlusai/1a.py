inFile = open("A-large.in")
inFile.readline()

outFile = open("A-large.out", "w")

caseNum = 1

for line in inFile:
    origNum = int(line.rstrip())
    num = origNum

    digits = set()

    cnt = 0

    while(len(digits) < 10):
        for digit in str(num):
            digits.add(digit)
        if(len(digits) < 10):
            num += origNum
        else:
            print("Case #" + str(caseNum) + ":", num, file=outFile)
            break
        cnt += 1

        if(cnt > 100000000):
            print("Case #" + str(caseNum) + ":", "INSOMNIA", file=outFile)
            break
        
    caseNum += 1

outFile.close()
