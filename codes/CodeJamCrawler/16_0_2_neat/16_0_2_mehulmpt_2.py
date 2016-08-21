case = input()
case = int(case)

def rev(stringX):
    for i in range(0,len(stringX)):
        if(stringX[i] == '+'):
            stringX[i] = '-'
        elif(stringX[i] == '-'):
            stringX[i] = '+'
    return stringX

for i in range(0, case):
    stringLol = input()
    stringX = list(stringLol)
    counter = 0
    for j in range(1,len(stringX)+1):
        #print(stringX)
        if(stringX[-j] == '+'):
            stringX[-j] = 'X'
            pass
        elif(stringX[-j] == '-'):
            counter = counter + 1
            stringX = rev(stringX)
            j=1
    print('Case #'+str(i+1)+': '+str(counter))

