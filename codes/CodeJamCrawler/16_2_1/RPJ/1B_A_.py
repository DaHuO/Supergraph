EX = 'A'
#SAMPLE = 'sample'
#SAMPLE = 'small'
SAMPLE = 'large'

def getPhone(phoneStr):
    phoneLst = list(phoneStr.upper())
    numbers = []

    lstD = list('ZERO')
    while 'Z' in phoneLst:
        numbers.append(0)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('TWO')
    while 'W' in phoneLst:
        numbers.append(2)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('SIX')
    while 'X' in phoneLst:
        numbers.append(6)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('EIGHT')
    while 'G' in phoneLst:
        numbers.append(8)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('THREE')
    while 'H' in phoneLst:
        numbers.append(3)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('FOUR')
    while 'U' in phoneLst:
        numbers.append(4)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('FIVE')
    while 'F' in phoneLst:
        numbers.append(5)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('SEVEN')
    while 'V' in phoneLst:
        numbers.append(7)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('ONE')
    while 'O' in phoneLst:
        numbers.append(1)
        for i in lstD:
            phoneLst.remove(i)

    lstD = list('NINE')
    while 'N' in phoneLst:
        numbers.append(9)
        for i in lstD:
            phoneLst.remove(i)

    return ''.join(str(i) for i in sorted(numbers))


if __name__ == '__main__':
    inputNb = None
    outputFile = open(r'Data\1B_%s_%s.out' % (EX, SAMPLE), 'w')
    for i, line in enumerate(open(r'Data\A-large.in')):
        if not inputNb:
            inputNb = int(line)
            continue
        outputFile.write('Case #%s: %s\n' % (i, getPhone(line.strip())))
    outputFile.close()



