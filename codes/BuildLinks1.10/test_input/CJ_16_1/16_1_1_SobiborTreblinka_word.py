import sys

file = open(sys.argv[1], 'r')
file.readline()

caseNumber = 1

for case in file:
    word = case.rstrip()

    array = []

    for letter in case:
        if len(array) == 0:
            array.append(letter)
        else:
            firstOrdinal = ord(array[0])
            letterOrdinal = ord(letter)

            if letterOrdinal >= firstOrdinal:
                array.insert(0, letter)
            else:
                array.append(letter)
    print 'Case #{}: {}'.format(caseNumber, ''.join(array).rstrip())

    caseNumber += 1