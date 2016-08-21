def parse(num):
    res = []
    num = list(num)
    try:
        while 'Z' in num:
            num.pop(num.index('Z'))
            num.pop(num.index('E'))
            num.pop(num.index('R'))
            num.pop(num.index('O'))
            res.append('0')
    except ValueError:
        pass
    try:
        while 'X' in num:
            num.pop(num.index('S'))
            num.pop(num.index('I'))
            num.pop(num.index('X'))
            res.append('6')
    except ValueError:
        pass
    try:
        while 'G' in num:
            num.pop(num.index('E'))
            num.pop(num.index('I'))
            num.pop(num.index('G'))
            num.pop(num.index('H'))
            num.pop(num.index('T'))
            res.append('8')
    except ValueError:
        pass
    try:
        while 'W' in num:
            num.pop(num.index('T'))
            num.pop(num.index('W'))
            num.pop(num.index('O'))
            res.append('2')
    except ValueError:
        pass
    try:
        while 'T' in num:
            num.pop(num.index('T'))
            num.pop(num.index('H'))
            num.pop(num.index('R'))
            num.pop(num.index('E'))
            num.pop(num.index('E'))
            res.append('3')
    except ValueError:
        pass
    try:
        while 'S' in num:
            num.pop(num.index('S'))
            num.pop(num.index('E'))
            num.pop(num.index('V'))
            num.pop(num.index('E'))
            num.pop(num.index('N'))
            res.append('7')
    except ValueError:
        pass
    try:
        while 'R' in num:
            num.pop(num.index('F'))
            num.pop(num.index('O'))
            num.pop(num.index('U'))
            num.pop(num.index('R'))
            res.append('4')
    except ValueError:
        pass
    try:
        while 'V' in num:
            num.pop(num.index('F'))
            num.pop(num.index('I'))
            num.pop(num.index('V'))
            num.pop(num.index('E'))
            res.append('5')
    except ValueError:
        pass
    try:
        while 'O' in num:
            num.pop(num.index('O'))
            num.pop(num.index('N'))
            num.pop(num.index('E'))
            res.append('1')
    except ValueError:
        pass
    try:
        while 'I' in num:
            num.pop(num.index('N'))
            num.pop(num.index('I'))
            num.pop(num.index('N'))
            num.pop(num.index('E'))
            res.append('9')
    except ValueError:
        pass
    res.sort()
    return ''.join(res)


if __name__ == '__main__':
    T = input()
    for i in range(T):
        inp = raw_input()
        print "Case #{}: {}".format(i+1, parse(inp))