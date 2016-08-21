import sys
import math

inputFile = open('C-small-attempt1.in');
outputFile = open('output.txt', 'w');
numberOfCases = inputFile.readline();

def findDivisor(number):
    if number < 2: return False;
    if number == 2: return False;
    if number == 3: return False;

    for i in range(6, math.ceil(number**0.5), 6):
        if number % (i-1) == 0:
            return i-1;
        if number % (i+1) == 0:
            return i+1;

    return False;

for case in range(1, int(numberOfCases)+1):

    outputFile.write('Case #' + str(case) + ':\n')

    data = inputFile.readline();
    
    data = data.split(' ');
    
    coinLength = int(data[0]);
    numCoins = int(data[1]);
    coinCount = 0;
    middleNum = '0'*(coinLength-2);

    while coinCount < numCoins:
        num = '1' + middleNum + '1';
        coinValues = [
            int(num, 2),
            int(num, 3),
            int(num, 4),
            int(num, 5),
            int(num, 6),
            int(num, 7),
            int(num, 8),
            int(num, 9),
            int(num, 10),
        ]
        
        divisors = [];

        validCoin = True;
        for value in coinValues:
            divisor = findDivisor(value);
            if divisor:
                divisors.append(divisor);
            else:
                validCoin = False;
                break;

        if validCoin:
            coinCount += 1;
            outputFile.write(num + ' ' + ' '.join(str(i) for i in  divisors) + '\n');

        middleNum = "{0:b}".format(int(middleNum, 2)+1);
        middleNum = '0'*(coinLength-2-len(middleNum)) + middleNum;
            

inputFile.close();
outputFile.close();    

