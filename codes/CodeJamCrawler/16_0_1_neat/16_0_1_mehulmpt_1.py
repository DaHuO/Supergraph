cases = input()
cases = int(cases)

def done(reqNums):
    for i in range (0,10):
        if i in reqNums:
            pass
        else:
            return False
    return True

for j in range(0,cases):
    k = 2
    inputX = input()
    inputX = int(inputX)
    if inputX == 0:
        print('Case #'+str(j+1)+': INSOMNIA')
    else:
        reqNums = set()
        oldNum = inputX
        while 1==1:
            tmpIn = inputX
            while 1==1:
                c = inputX % 10
                inputX = inputX - c
                inputX = inputX/10
                reqNums.add(c)
                if(inputX == 0):
                    break
            #print(reqNums)
            if(done(reqNums)):
                print('Case #'+str(j+1)+': '+str(tmpIn))
                break
            else:
                inputX = k*oldNum
                k = k+1
                #print(k)





