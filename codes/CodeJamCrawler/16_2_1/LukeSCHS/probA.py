#By Luke Baird for Google CodeJam Round 1b 2016
#problem A - Getting the Digits

for x in range(int(input())):
    mString = input()
    mString = list(mString)
    numbers = []
    while 'Z' in mString:
        #pull out 'Z', 'E', 'R', 'O',
        mString.remove('Z')
        mString.remove('E')
        mString.remove('R')
        mString.remove('O')
        numbers.append(0)
    while 'X' in mString:
        mString.remove('S')
        mString.remove('I')
        mString.remove('X')
        numbers.append(6)
    while 'U' in mString:
        mString.remove('F')
        mString.remove('O')
        mString.remove('U')
        mString.remove('R')
        numbers.append(4)
    while 'W' in mString:
        mString.remove('T')
        mString.remove('W')
        mString.remove('O')
        numbers.append(2)
    while 'G' in mString:
        mString.remove('E')
        mString.remove('I')
        mString.remove('G')
        mString.remove('H')
        mString.remove('T')
        numbers.append(8)
    while 'H' in mString:
        mString.remove('T')
        mString.remove('R')
        mString.remove('H')
        mString.remove('E')
        mString.remove('E')
        numbers.append(3)
    while 'O' in mString:
        mString.remove('O')
        mString.remove('N')
        mString.remove('E')
        numbers.append(1)
    while 'F' in mString:
        mString.remove('F')
        mString.remove('I')
        mString.remove('V')
        mString.remove('E')
        numbers.append(5)
    while 'V' in mString:
        mString.remove('S')
        mString.remove('E')
        mString.remove('V')
        mString.remove('E')
        mString.remove('N')
        numbers.append(7)
    while 'I' in mString:
        mString.remove('I')
        # we can cheat with 9 - NINE
        numbers.append(9)
    numbers.sort()
    rS = ""
    for val in numbers:
        rS += str(val)
    print(str.format("Case #{}: {}", x+1, rS))