testCaseNums = list()

def getLastNum(num):
    multiple = 1
    num_basket = list()
    realnum = num

    while(len(num_basket)<10):
        num = 0;
        num = realnum*multiple
        num = str(num)
        for i in range(len(num)):
            num_basket.append(num[i])
            num_basket = list(set(num_basket))
            num_basket.sort()

        multiple = multiple+1
        num = int(num)

    return num;

def getCaseResult(num):
    if num==0:
        return "INSOMNIA"
    elif num>0:
        return getLastNum(num)


testCaseCount = input()

for i in range(testCaseCount):
    num = input()
    testCaseNums.append(num)
j = 1

for i in testCaseNums:
    print("Case #%d: %s"%(j,getCaseResult(i)))
    j = j+1

