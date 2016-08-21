def getLastNumber(case,firstNumber):
    catcher = [0]*10
    if(int(firstNumber) == 0):
        print('Case #' +str(case) +': INSOMNIA')
    else:
        counter = 1
        finalNumber = firstNumber
        while(True):
            digits = list(str(finalNumber).strip())
            digits = [int(i) for i in digits]
            counter = counter + 1
            for i in digits:
                if(catcher[i]==0):
                    catcher[i] = 1
            if 0 not in catcher:
                break
            finalNumber = int(firstNumber) * counter
        print('Case #' +str(case) +': '+ str(finalNumber))

with open('counting-sheep-input.txt', 'r') as f:
    next(f)
    case = 1;
    for line in f:
        getLastNumber(case,line)
        case+=1
