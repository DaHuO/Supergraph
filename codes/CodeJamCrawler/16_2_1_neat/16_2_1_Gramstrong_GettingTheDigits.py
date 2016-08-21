import sys

inputFile = open('A-large.in');
outputFile = open('output.txt', 'w');
numberOfCases = inputFile.readline();

first = {
    'Z': [0,'ZERO'],
    'W': [2, 'TWO'],
    'U': [4, 'FOUR'],
    'X': [6, 'SIX'],
    'G': [8, 'EIGHT']
}

second = {
    'O': [1,'ONE'],
    'R': [3, 'THREE'],
    'F': [5, 'FIVE'],
    'S': [7, 'SEVEN'],
}

third = {
    'I': [9, 'NINE']
}

for case in range(1, int(numberOfCases)+1):
    string = inputFile.readline();
    number = [];

    for c in string:
        if c in first:
            number.append(str(first[c][0]))
            for each in first[c][1]:
                string = string.replace(each, '', 1)

    for c in string:
        if c in second:
            number.append(str(second[c][0]))
            for each in second[c][1]:
                string = string.replace(each, '', 1)
    for c in string:
        if c in third:
            number.append(str(third[c][0]))
            for each in third[c][1]:
                string = string.replace(each, '', 1)

    number = sorted(number, key=int)
    outputFile.write('Case #' + str(case) + ': ' + ''.join(number) + '\n');

inputFile.close();
outputFile.close();    

