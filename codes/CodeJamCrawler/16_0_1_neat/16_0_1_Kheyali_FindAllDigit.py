def findEndNumber(num):
    if num == 0:
        return "INSOMNIA"

    digitContainer = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,0:False}
    digitToBeFound = 10
    currentNumber = num
    for i in range(1,1000):
        divisor = 1
        currentNumber = num*i
        while divisor <= currentNumber:
            digit = int((currentNumber%(divisor*10))/(divisor))
            if digitContainer[digit] == False:
                digitContainer[digit] = True
                digitToBeFound = digitToBeFound -1
                if(digitToBeFound <= 0):
                    return currentNumber
            divisor = divisor*10
    return "INSOMNIA"



testCases = int(input().strip())
for i in range(testCases):
    actualNo = findEndNumber(int(input().strip()))
    print("Case #"+str(i+1)+": " + str(actualNo))