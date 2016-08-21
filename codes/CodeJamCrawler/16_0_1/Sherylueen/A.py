

caseNum = int(raw_input())
for i in range(caseNum):
    numSet = ()
    inputStr = raw_input()
    inputInt = int(inputStr)  
    tempSet = set(inputStr)
    tempStr = inputStr
    tempInt = inputInt
    multiTime = 2
    while True:
        if not inputInt:
            print 'Case #'+str(i+1)+': INSOMNIA'
            break
        if len(tempSet)== 10:
            print 'Case #'+str(i+1)+': '+tempStr
            break
        tempInt = inputInt*multiTime
        tempStr = str(tempInt)
        tempSet.update(tempStr)
        multiTime += 1  



