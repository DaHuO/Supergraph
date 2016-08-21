
file = open("c:/project/codejam/2016/A-large.in", 'r')
data = file.read()
file.close()
#print data

tokens = data.strip().split('\n')
resultList = []
for idx in range(1, len(tokens)):
    numStr = tokens[idx].strip()
    if(0 == int(numStr)):
        resultList.append(0)
        continue
    
    numList = []
    for i in range(0, len(numStr)):
        numList.append(int(numStr[i]))
    numList.reverse()  
    print "start: " + numStr
    num = numList[0:len(numList)]
    checkNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while(True):      
        for i in range(0, len(numList)):
            checkNum[numList[i]] = 1
        
        isClear = True
        for i in range(0, 10):
            if(0 == checkNum[i]):
                isClear = False
        
        if(True == isClear):
            break
        
        for i in range(0, len(num)):
            sum = numList[i] + num[i]
            if(10 <= sum):
                numList[i] = sum % 10
                nextIndex = i + 1
                if(len(numList) == nextIndex):
                    numList.append(sum / 10)
                else:
                    numList[nextIndex] = numList[nextIndex] + sum / 10
            else:
                numList[i] = sum
        
        print numList
    
    result = 0
    for i in range(0, len(numList)):
        result = result + numList[i] * pow(10, i)
    
    print "---" + str(result)
    resultList.append(result)

data = ""
for i in range(0, len(resultList)):
    if(0 == resultList[i]):
        data = data + "Case #" + str(i + 1) + ": INSOMNIA\n"
    else:
        data = data + "Case #" + str(i + 1) + ": " + str(resultList[i]) + "\n"

data = data.strip()
print data  
file = open('c:/project/codejam/2016/output.txt', 'w')
file.write(data)
file.close()
    
             
        
