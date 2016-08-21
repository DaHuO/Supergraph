casos = int(input())
for a in range(1,casos + 1):
    number = []
    strr = str(input())
    while 'Z' in list(strr):
        strr = strr.replace('Z','',1)
        strr = strr.replace('E','',1)
        strr = strr.replace('R','',1)
        strr = strr.replace('O','',1)
        number.append('0')
    # print('zero ' + strr)
    while 'W' in list(strr):
        strr = strr.replace('T','',1)
        strr = strr.replace('W','',1)
        strr = strr.replace('O','',1)
        number.append('2')
    while 'U' in list(strr):
        strr = strr.replace('F','',1)
        strr = strr.replace('O','',1)
        strr = strr.replace('U','',1)
        strr = strr.replace('R','',1)
        number.append('4')
    while 'X' in list(strr):
        strr = strr.replace('S','',1)
        strr = strr.replace('I','',1)
        strr = strr.replace('X','',1)
        number.append('6')

    while 'G' in list(strr):
        strr = strr.replace('E','',1)
        strr = strr.replace('I','',1)
        strr = strr.replace('G','',1)
        strr = strr.replace('H','',1)
        strr = strr.replace('T','',1)
        number.append('8')

    while 'F' in list(strr):
        strr = strr.replace('F','',1)
        strr = strr.replace('I','',1)
        strr = strr.replace('V','',1)
        strr = strr.replace('E','',1)
        number.append('5')

    while 'T' in list(strr):
        strr = strr.replace('T','',1)
        strr = strr.replace('H','',1)
        strr = strr.replace('R','',1)
        strr = strr.replace('E','',1)
        strr = strr.replace('E','',1)
        number.append('3')

    while 'O' in list(strr):
        strr = strr.replace('O','',1)
        strr = strr.replace('N','',1)
        strr = strr.replace('E','',1)
        number.append('1')

    while 'I' in list(strr):
        strr = strr.replace('N','',1)
        strr = strr.replace('I','',1)
        strr = strr.replace('N','',1)
        strr = strr.replace('E','',1)
        number.append('9')

    while 'S' in list(strr):
        strr = strr.replace('S','',1)
        strr = strr.replace('E','',1)
        strr = strr.replace('V','',1)
        strr = strr.replace('E','',1)
        strr = strr.replace('N','',1)
        number.append('7')
    number.sort()
    print("Case #{}: ".format(a) + "".join(number))
