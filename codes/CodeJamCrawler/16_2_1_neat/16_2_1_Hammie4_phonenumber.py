inputfile = open('inputfile.txt', 'r')
outputfile = open('outputfile.txt', 'w')

for num, line in enumerate(inputfile,1):
    if (num > 1):
        letters = []
        numbers = []
        for char in line:
#            print char
            letters.append(char)
        #remove 4s
        while(letters.count('U') > 0):
            letters.remove('F')
            letters.remove('O')
            letters.remove('U')
            letters.remove('R')
            numbers.append(4)
        while(letters.count('G') > 0):
            letters.remove('E')
            letters.remove('I')
            letters.remove('G')
            letters.remove('H')
            letters.remove('T')
            numbers.append(8)
        while(letters.count('F') > 0):
            letters.remove('F')
            letters.remove('I')
            letters.remove('V')
            letters.remove('E')
            numbers.append(5)
        while(letters.count('V') > 0):
            letters.remove('S')
            letters.remove('E')
            letters.remove('V')
            letters.remove('E')
            letters.remove('N')
            numbers.append(7)
        while(letters.count('Z') > 0):
            letters.remove('Z')
            letters.remove('E')
            letters.remove('R')
            letters.remove('O')
            numbers.append(0)
        while(letters.count('X') > 0):
            letters.remove('S')
            letters.remove('I')
            letters.remove('X')
            numbers.append(6)
        while(letters.count('I') > 0):
            letters.remove('N')
            letters.remove('I')
            letters.remove('N')
            letters.remove('E')
            numbers.append(9)
        while(letters.count('W') > 0):
            letters.remove('T')
            letters.remove('W')
            letters.remove('O')
            numbers.append(2)
        while(letters.count('N') > 0):
            letters.remove('O')
            letters.remove('N')
            letters.remove('E')
            numbers.append(1)
        while(letters.count('E') > 0):
            letters.remove('T')
            letters.remove('H')
            letters.remove('R')
            letters.remove('E')
            letters.remove('E')
            numbers.append(3)
        numbers.sort()
        outputfile.write('Case #'+ str((num -1)) + ': ')
        for eachnum in numbers:
            outputfile.write(str(eachnum))
        outputfile.write('\n')
        





inputfile.close()
outputfile.close()
