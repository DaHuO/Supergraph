fdr = open("A-large.in.txt",'r')
fdw = open("output.txt",'w')

T = fdr.readline()

for i in range(int(T)):

    a = fdr.readline()
    a = list(a)
    number = []

    while 'Z' in a:
        a.remove('Z')
        a.remove('E')
        a.remove('R')
        a.remove('O')
        number.append(0)

    while 'X' in a:
        a.remove('S')
        a.remove('I')
        a.remove('X')
        number.append(6)

    while 'S' in a:
        a.remove('S')
        a.remove('E')
        a.remove('V')
        a.remove('E')
        a.remove('N')
        number.append(7)

    while 'W' in a:
        a.remove('T')
        a.remove('W')
        a.remove('O')
        number.append(2)

    while 'U' in a:
        a.remove('F')
        a.remove('O')
        a.remove('U')
        a.remove('R')
        number.append(4)

    while 'F' in a:
        a.remove('F')
        a.remove('I')
        a.remove('V')
        a.remove('E')
        number.append(5)

    while 'G' in a:
        a.remove('E')
        a.remove('I')
        a.remove('G')
        a.remove('H')
        a.remove('T')
        number.append(8)

    while 'H' in a:
        a.remove('T')
        a.remove('H')
        a.remove('R')
        a.remove('E')
        a.remove('E')
        number.append(3)

    while 'O' in a:
        a.remove('O')
        a.remove('N')
        a.remove('E')
        number.append(1)

    while 'N' in a:
        a.remove('N')
        a.remove('I')
        a.remove('N')
        a.remove('E')
        number.append(9)

    number.sort()
    number_str = ''.join(str(j) for j in number)
    fdw.write("case #" + str(i+1) + ": " + number_str+'\n')

fdr.close()
fdw.close()
