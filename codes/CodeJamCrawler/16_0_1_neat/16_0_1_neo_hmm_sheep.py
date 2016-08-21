'''
Created on Apr 9, 2016

@author: Hari
'''
def findNum(initialNum):
    if initialNum == 0:
        return "INSOMNIA";
    
    digits = set();
    x = 1;
    while len(digits) < 10:
        num = initialNum * x;
        lastNum = num;
        strNum = str(num);
        for ch in strNum:
            digits.add(ch);
        x = x + 1;
    
    return lastNum;
    
t = int(input());
for i in range(1, t + 1):
    num = input();
    answer = findNum(int(num));
    print("Case #{}: {}".format(i, answer));

    