'''
Created on Apr 16, 2016

@author: Hari
'''

def createMaxStr(inputStr):
    newStr = inputStr[0];
    remStr = inputStr[1:]
    for ch in remStr:
        if ch >= newStr[0]:
            newStr = ch + newStr;
        else:
            newStr = newStr + ch;
    return newStr;

t = int(input());
for i in range(1, t + 1):
    origStr = input();
    print("Case #{}: {}".format(i, createMaxStr(origStr))); 
    

            
        