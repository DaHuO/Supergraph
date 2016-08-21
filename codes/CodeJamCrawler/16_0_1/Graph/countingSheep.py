f = open('countingSheepTest.txt', 'r')
output = open('sheepResults.txt', 'w+')
numOfTests = f.readline()
count = 0
for line in f:
    count += 1
    testNum = line.strip()
    num = str(testNum)
    if num == '0':
        output.write("Case #"+str(count)+": INSOMNIA\n")
    else:
        digitsSeen = ""
        loopCount = 1
        while len(digitsSeen) != 10:
            for char in num:
                if char not in digitsSeen:
                    digitsSeen += char
                    print digitsSeen
                    if len(digitsSeen) == 10:
                        output.write("Case #" + str(count) + ": " + str(num) + "\n")
                        break
            else:

                loopCount += 1
                num = str(int(testNum) * loopCount)
                print num
