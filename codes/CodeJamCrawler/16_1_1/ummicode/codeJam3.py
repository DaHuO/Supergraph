#!/usr/bin/python

t = int(input())

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(1, t + 1):
    inputToken = raw_input()
    tokenList = list(inputToken)
    finalList = []
    for item in tokenList:
        #print alphabet.index(item)
        if not finalList:
            finalList.append(item)
        else:
            if alphabet.index(finalList[0]) > alphabet.index(item):
                finalList.append(item)
            else:
                finalList.insert(0, item)
      
    finalWord = ''.join(map(str, finalList))   
    print("Case #{}: {}".format(i, finalWord))
