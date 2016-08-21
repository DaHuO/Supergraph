import sys

inputFile = open('A-large.in');
outputFile = open('output.txt', 'w');
numberOfCases = inputFile.readline();

for case in range(1, int(numberOfCases)+1):
    digits = set(['0','1','2','3','4','5','6','7','8','9']);
    testNumber = int(inputFile.readline());
    multiplier = 1;

    if(testNumber == 0):
        outputFile.write('Case #' + str(case) + ': INSOMNIA\n');
    else:
        while digits:
            lastNumber = testNumber * multiplier;
            digits = digits - set(str(lastNumber));
            multiplier += 1;
        
        outputFile.write('Case #' + str(case) + ': ' + str(lastNumber) + '\n'); 

inputFile.close();
outputFile.close();    

