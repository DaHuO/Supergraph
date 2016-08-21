def deleteCharacters(chars, l):
    for c in chars:
        l = l.replace(c, '', 1)
    return l

inputFile = open('A-large.in', 'r')
lines = [number.replace('\n', '') for number in inputFile.readlines()[1:]]
outputFile = open('output.txt', 'w')
counter = 1
for line in lines:
    outputFile.write('Case #{0}: '.format(counter))
    number = []
    while 'G' in line:
        number.append(8)
        line = deleteCharacters('EIGHT', line)
    while 'Z' in line:
        number.append(0)
        line = deleteCharacters('ZERO', line)
    while 'U' in line:
        number.append(4)
        line = deleteCharacters('FOUR', line)
    while 'X' in line:
        number.append(6)
        line = deleteCharacters('SIX', line)
    while 'W' in line:
        number.append(2)
        line = deleteCharacters('TWO', line)
    while 'H' in line:
        number.append(3)
        line = deleteCharacters('THREE', line)
    while 'F' in line and 'I' in line and 'V' in line and 'E' in line:
        number.append(5)
        line = deleteCharacters('FIVE', line)
    while 'S' in line and 'E' in line and 'V' in line and 'N' in line:
        number.append(7)
        line = deleteCharacters('SEVEN', line)
    while 'O' in line and 'N' in line and 'E' in line:
        number.append(1)
        line = deleteCharacters('ONE', line)
    while 'N' in line and 'I' in line and 'E' in line:
        number.append(9)
        line = deleteCharacters('NINE', line)
    for n in sorted(number):
        outputFile.write('{0}'.format(n))
    outputFile.write('\n')
    counter += 1
