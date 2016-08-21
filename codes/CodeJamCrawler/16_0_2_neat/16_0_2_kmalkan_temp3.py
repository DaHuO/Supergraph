def getNumFlips(pancakes):
    numFlips=0
    currentRunningState=pancakes[0]
    for pancakeIndex in range(1,len(pancakes)):
        if pancakes[pancakeIndex]==currentRunningState:
            continue
        currentRunningState=pancakes[pancakeIndex]
        numFlips+=1
    if currentRunningState=='-':
        numFlips+=1
    return numFlips

def printResults(answers):
    for i in range(0,len(answers)):
        print "Case #"+str(i+1)+": "+str(answers[i])


num_cases=int(raw_input())
answers=[]
for i in range(0,num_cases):
    pancakes=raw_input()
    if len(pancakes)==0:
        answers.append(0)
        continue
    numFlips=getNumFlips(pancakes)
    answers.append(numFlips)
printResults(answers)

