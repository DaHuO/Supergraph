def getLines(filename):
    with open(filename) as f:
        return f.readlines()


def appendToFile(filename, text):
    with open(filename,'a') as f:
        f.write(text + '\n')

def getDigits(n):
    res = []
    while (True):
        res.append(n%10)
        n /= 10
        if n == 0:
            return res

lines = getLines('A-large.in')
testsNum = int(lines[0])

for lineNum in xrange(1,testsNum + 1):
    seenDigits = []
    line = lines[lineNum]

    n = int(line)
    originalN = n

    counter = 0
    while len(seenDigits) < 10:
        digits = getDigits(n)

        for digit in digits:
            if digit not in seenDigits:
                seenDigits.append(digit)

        n += originalN
        counter+=1

        if counter == 1000:
            break

    if counter == 1000:
        appendToFile('output.txt', "Case #"+str(lineNum) + ": " + "INSOMNIA")
        continue

    appendToFile('output.txt', "Case #"+str(lineNum) + ": " + str(n - originalN))


