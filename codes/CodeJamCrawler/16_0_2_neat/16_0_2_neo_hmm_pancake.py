'''
Created on Apr 9, 2016

@author: Hari
'''

FLIP = {"-": "+", "+": "-"};

def flipStr(origStr):
    s = origStr.replace("+","$");
    s = s.replace("-","+");
    s = s.replace("$","-");
    return s[::-1];

t = int(input());
for i in range(1, t + 1):
    origStr = input();
    c = 0;
    happy = False;
    l = len(origStr);
    flipEnd = l - 1;

    while not happy:
        while origStr[flipEnd] == "+" and flipEnd > -1:
            flipEnd = flipEnd - 1;
        
        if flipEnd == -1:
            happy = True;
            break;
    
        if origStr[0] == "+":
            c = c + 1;
            countFlip = 1;
            while origStr[countFlip] == "+":
                countFlip = countFlip + 1;
            origStr = origStr.replace("+", "-", countFlip);
            #print ("Count is {}, current stack is {}".format(c, origStr))
    
        c = c + 1;
        cutStr , remStr = origStr[: flipEnd + 1], origStr[flipEnd + 1: ];
        cutStr = flipStr(cutStr);
        origStr = cutStr + remStr;
        #print ("Count is {}, current stack is {}".format(c, origStr))
    
    print("Case #{}: {}".format(i, c));
          