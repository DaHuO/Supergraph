
f = open("A-large.in")
fw = open("output.txt", 'w+')

testCases = 0
checkArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

first_line = f.readline()
testCases = int(first_line)

def checkINSOMNIA():
    for i in xrange(0, 10):
        if checkArray[i] == 0:
            return True
        pass
    return False
    pass

for i in xrange(0, testCases):

    n = int(f.readline()) # N
    bigN = n
    multiplayerIndex = 1
    checkArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # reset

    if n == 0:
        fw.write('Case #{}: INSOMNIA\n'.format(i+1))
        continue

    while checkINSOMNIA():

        n = bigN * multiplayerIndex
        lastNumberBeforeSleep = n

        while n:
            digit = n % 10
            checkArray[digit] = 1 # mark as found
            n = n / 10
            pass

        multiplayerIndex += 1
        pass

    fw.write('Case #{}: {}\n'.format(i+1, lastNumberBeforeSleep))
    pass

f.close()
fw.close()
