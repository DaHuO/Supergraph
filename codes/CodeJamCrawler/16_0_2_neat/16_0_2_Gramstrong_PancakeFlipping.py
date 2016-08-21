import sys

inputFile = open('B-large.in');
outputFile = open('output.txt', 'w');
numberOfCases = inputFile.readline();

happy = '+';
sad = '-';

for case in range(1, int(numberOfCases)+1):
    pancakeStack = list(reversed(inputFile.readline()));

    flips = 0;
    pancakeStackHeight = len(pancakeStack);

    for i in range(0, pancakeStackHeight):
        if pancakeStack[i] is sad and not (flips % 2):
            flips += 1;
        elif pancakeStack[i] is happy and (flips % 2):
            flips += 1;

    
    outputFile.write('Case #' + str(case) + ': ' + str(flips) + '\n'); 

inputFile.close();
outputFile.close();    

