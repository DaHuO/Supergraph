
def gotosleep(num, numlist):
    sleeplist = numlist
    counter = 1
    addNum = num
    while sleeplist != []:
            for i in str(addNum):
                if int(i) in sleeplist:
                    sleeplist.remove(int(i))
            counter = counter + 1
            if sleeplist != []:
                addNum = num*counter
    return addNum

caseNum = 1

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if n != 0:
        output = gotosleep(n, numlist)
    else:
        output = "INSOMNIA"
    print("%s%d%s%s" % ("Case #", caseNum, ": ", str(output)))
    caseNum = caseNum + 1
