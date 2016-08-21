'''
Created on Apr 10, 2016

@author: apple
'''


    
def getLastNum(initNum):
    if initNum == 0:
        return "INSOMNIA"
    numSet = set()
    i = 1
    while(len(numSet)!=10):
        numSet |= getDigitByNum(initNum*i)
        i += 1
    
    return initNum*(i-1)

def getDigitByNum(num):
    numSet = set()
    while(num // 10 != 0) :
        numSet.add(num % 10)
        num = num//10
    numSet.add(num%10)
    return numSet

def formatPrint(res):
    print("Case %i")
    

totalNum = int(raw_input())
formatString = "Case #%d: %s"

for i in xrange(1, totalNum+1):
    num = int(raw_input())
    print formatString % (i, getLastNum(num))
    

    
#     if not firstFlag:
#         firstFlag = True
#         continue
#     print formatString % (count, getLastNum(int(line)))
#     count += 1
    