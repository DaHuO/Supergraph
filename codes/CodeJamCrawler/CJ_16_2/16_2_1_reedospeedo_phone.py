f = open('a-large.in', 'r')
t = int(f.readline())
output_file = open('a-large.out', 'w')
for i in xrange(1, t+1):
    split = [s for s in f.readline().strip()]
    number = []
    letter = 0
    while 'Z' in split:
        number.append('0')
        split.remove('Z')
        if 'O' in split:
            split.remove('O')
        if 'R' in split:
            split.remove('R')
        if 'E' in split:
            split.remove('E')

    while 'W' in split:
        number.append('2')
        split.remove('W')
        if 'O' in split:
            split.remove('O')
        if 'T' in split:
            split.remove('T')

    while 'G' in split:
        number.append('8')
        if 'E' in split:
            split.remove('E')
        if 'I' in split:
            split.remove('I')
        if 'G' in split:
            split.remove('G')
        if 'H' in split:
            split.remove('H')
        if 'T' in split:
            split.remove('T')

    while 'U' in split:
        number.append('4')
        if 'F' in split:
            split.remove('F')
        if 'O' in split:
            split.remove('O')
        if 'U' in split:
            split.remove('U')
        if 'R' in split:
            split.remove('R')

    while 'F' in split:
        if 'F' in split:
            split.remove('F')
        if 'I' in split:
            split.remove('I')
        if 'V' in split:
            split.remove('V')
        if 'E' in split:
            split.remove('E')
        number.append('5')

    while 'O' in split:
        number.append('1')
        if 'O' in split:
            split.remove('O')
        if 'N' in split:
            split.remove('N')
        if 'E' in split:
            split.remove('E')

    while 'H' in split:
        number.append('3')
        if 'T' in split:
            split.remove('T')
        if 'H' in split:
            split.remove('H')
        if 'R' in split:
            split.remove('R')
        if 'E' in split:
            split.remove('E')
        if 'E' in split:
            split.remove('E')

    while 'X' in split:
        number.append('6')
        if 'S' in split:
            split.remove('S')
        if 'I' in split:
            split.remove('I')
        if 'X' in split:
            split.remove('X')

    while 'V' in split:
        number.append ('7')
        if 'S' in split:
            split.remove('S')
        if 'E' in split:
            split.remove('E')
        if 'V' in split:
            split.remove('V')
        if 'E' in split:
            split.remove('E')
        if 'N' in split:
            split.remove('N')

    while 'I' in split:
        number.append('9')
        if 'N' in split:
            split.remove('N')
        if 'I' in split:
            split.remove('I')
        if 'N' in split:
            split.remove('N')
        if 'E' in split:
            split.remove('E')

    print number
    string = ''.join(sorted(number))
    print string
    output_file.write("Case #%d: %s\n" % (i, string))

output_file.close()