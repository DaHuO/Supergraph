#!/usr/bin/python

maxTestCases = int(raw_input().strip())

for caseNum in xrange(1, maxTestCases + 1):
    origSheep = int(raw_input().strip())
    answer = 'INSOMNIA'

    sheepList = [False] * 10

    count = 0
    sheepFound = False
    while not sheepFound:
        count += 1
        sheepCount = origSheep * count

        # Check for 0 sheep
        if sheepCount == 0:
            break

        # Deduplicate the digits
        sheepSet = set(str(sheepCount))

        for digit in sheepSet:
            sheepList[int(digit)] = True

        sheepFound = reduce(lambda x, y: x and y, sheepList)
        if sheepFound:
            answer = sheepCount

    print 'Case #{}: {}'.format(caseNum, answer)
