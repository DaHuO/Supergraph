

def remove(text, r):
    for i in r:
        text = text.replace(i, '', 1)
    return text


def getting_the_digits(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')
    
    for i in range(T):
        num = []
        text = fr.readline()
        while 'Z' in text:
            num.append(0)
            text = remove(text, 'ZERO')
        while 'W' in text:
            num.append(2)
            text = remove(text, 'TWO')
        while 'U' in text:
            num.append(4)
            text = remove(text, 'FOUR')
        while 'X' in text:
            num.append(6)
            text = remove(text, 'SIX')
        while 'G' in text:
            num.append(8)
            text = remove(text, 'EIGHT')
        while 'O' in text:
            num.append(1)
            text = remove(text, 'ONE')
        while 'T' in text:
            num.append(3)
            text = remove(text, 'THREE')
        while 'F' in text:
            num.append(5)
            text = remove(text, 'FIVE')
        while 'S' in text:
            num.append(7)
            text = remove(text, 'SEVEN')
        while 'E' in text:
            num.append(9)
            text = remove(text, 'NINE')
            
#         print('Case #%d: '%(i+1) + ''.join(str(i) for i in sorted(num)))
        fw.write('Case #%d: '%(i+1) + ''.join(str(i) for i in sorted(num)) + '\n')

    fr.close()
    fw.close()


getting_the_digits('A-large.in')




