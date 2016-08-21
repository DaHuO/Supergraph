infile = open("A-large.in", "r")
outfile = open("A-large.out", "w")

ZERO = ['Z', 'E', 'R', 'O']
ONE = ['O', 'N', 'E']
TWO = ['T', 'W', 'O']
THREE = ['T', 'H', 'R', 'E', 'E']
FOUR = ['F', 'O', 'U', 'R']

t = infile.readline()
print(t)
casenumber = 1
for line in infile:
    s = list(line[:-1])
    number = []
    print(s)
    while s != []:
        if 'Z' in s:
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
            number.append('0')
        elif 'W' in s:
            s.remove('T')
            s.remove('W')
            s.remove('O')
            number.append('2')
        elif 'X' in s:
            s.remove('S')
            s.remove('I')
            s.remove('X')
            number.append('6')            
        elif 'G' in s:
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')
            number.append('8')
        elif 'F' in s:
            if 'R' in s and 'O' in s and 'U' in s:
                s.remove('F')
                s.remove('O')
                s.remove('U')
                s.remove('R')
                number.append('4')
            else:
                s.remove('F')
                s.remove('I')
                s.remove('V')
                s.remove('E')
                number.append('5')
        elif 'S' in s:
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')
            number.append('7')
        elif 'H' in s:
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')
            number.append('3')
        elif 'O' in s:
            s.remove('O')
            s.remove('N')
            s.remove('E')
            number.append('1')
        else:
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E')
            number.append('9')
        
    number.sort()

    print(number)
    print("Case #{}: ".format(casenumber), end='', file=outfile)
    for i in range(len(number)):
        print(number[i], end='', file=outfile)
    print('', file=outfile)
    casenumber+=1
        
print("done")
infile.close()
outfile.close()
