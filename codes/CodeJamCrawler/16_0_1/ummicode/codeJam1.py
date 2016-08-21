#!/usr/bin/python

t = int(input())
for i in range(1, t + 1):
    inNum = input()
    if inNum < 1:
        outVal = "INSOMNIA"
    else:
        stringArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        j = 1
        while True:
            currentNum = inNum*j
            strNum = str(currentNum)
            for item in strNum:
                try:
                    stringArray.remove(item)
                except:
                    pass
            j = j + 1
            outVal = currentNum
            if not stringArray:
                break
    print("Case #{}: {}".format(i, outVal))
