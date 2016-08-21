import os

fp = open('test')
of = open('output2016','w')
s = map(lambda x: x.strip(), fp.readlines())
s = s[1:]
cnt = 0
for string in s:
    num = []
    cnt += 1
    while string.count('$')!=len(string):
        string = list(string)
        while string.count('Z')>0:
            num.append('0')
            string[string.index('Z')] = '$'
            string[string.index('E')] = '$'
            string[string.index('R')] = '$'
            string[string.index('O')] = '$'
        while string.count('W') > 0:
            num.append('2')
            string[string.index('T')] = '$'
            string[string.index('W')] = '$'
            string[string.index('O')] = '$'
        while string.count('X') > 0:
            num.append('6')
            string[string.index('S')] = '$'
            string[string.index('I')] = '$'
            string[string.index('X')] = '$'
        while string.count('S') > 0:
            num.append('7')
            string[string.index('S')] = '$'
            string[string.index('E')] = '$'
            string[string.index('V')] = '$'
            string[string.index('E')] = '$'
            string[string.index('N')] = '$'
        while string.count('V') > 0:
            num.append('5')
            string[string.index('F')] = '$'
            string[string.index('I')] = '$'
            string[string.index('V')] = '$'
            string[string.index('E')] = '$'
        while string.count('G') > 0:
            num.append('8')
            string[string.index('E')] = '$'
            string[string.index('I')] = '$'
            string[string.index('G')] = '$'
            string[string.index('H')] = '$'
            string[string.index('T')] = '$'
        while string.count('F')>0:
            num.append('4')
            string[string.index('F')] = '$'
            string[string.index('O')] = '$'
            string[string.index('U')] = '$'
            string[string.index('R')] = '$'
        while string.count('O')>0:
            num.append('1')
            string[string.index('O')] = '$'
            string[string.index('N')] = '$'
            string[string.index('E')] = '$'
        while string.count('T') > 0:
            num.append('3')
            string[string.index('T')] = '$'
            string[string.index('H')] = '$'
            string[string.index('R')] = '$'
            string[string.index('E')] = '$'
            string[string.index('E')] = '$'
        while string.count('I') > 0:
            num.append('9')
            string[string.index('N')] = '$'
            string[string.index('I')] = '$'
            string[string.index('N')] = '$'
            string[string.index('E')] = '$'
    num = sorted(num)
    print >> of, 'Case #%d: %s' % (cnt, ''.join(num))




