import sys

def checkUse(isUsed, num):
    num = str(num)
    for i in num:
        isUsed[int(i)] = True
    return isUsed

caseNum = input()

for i in range(caseNum):
    case = i + 1
    count = 1
    isUsed = [False for i in xrange(10)]
    n = input()
    if n == 0:
        print "Case #{}: INSOMNIA".format(case)
        continue
    while True:
        isUsed = checkUse(isUsed, n * count)
        if False not in isUsed:
            break
        count += 1
        #print    isUsed

    print "Case #{0}: {1}".format(case, n*count)

