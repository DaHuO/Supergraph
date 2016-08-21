def getLastNum(N):
    currentNum=N
    if currentNum==0:
        return "INSOMNIA"
    seenSoFar=set()
    count=1
    while(True):
        seenSoFar=getDigits(currentNum,seenSoFar)
        if len(seenSoFar)==10:
            return currentNum

        count+=1
        currentNum=N*count

        if count>100000:
            return "INSOMNIA"

def getDigits(num,seenSoFar):
    while num!=0:
        lastDig=num%10
        num=num/10
        seenSoFar.add(lastDig)
    return seenSoFar

def printResults(i,lastNum,lln):
    print "Case #"+str(i+1)+": "+str(lastNum)

num_cases=int(raw_input())
N=num_cases
# print "Input\tOutput"
for i in range(0,num_cases):
    lln=N
    N=int(raw_input())
    lastNum=getLastNum(N)
    printResults(i,lastNum,lln)

