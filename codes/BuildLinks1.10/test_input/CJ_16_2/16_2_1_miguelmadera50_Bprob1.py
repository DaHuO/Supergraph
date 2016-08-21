def solution(string):
    num = ''
    while len(string) != 0:
        if 'Z' in string:
            string = string.replace('Z', '', 1)
            string = string.replace('E', '', 1)
            string = string.replace('R', '', 1)
            string = string.replace('O', '', 1)
            num += '0'
            continue
        if 'W' in string:
            string = string.replace('T', '', 1)
            string = string.replace('W', '', 1)
            string = string.replace('O', '', 1)
            num += '2'
            continue
        if 'X' in string:
            string = string.replace('S', '', 1)
            string = string.replace('I', '', 1)
            string = string.replace('X', '', 1)
            num += '6'
            continue
        if 'U' in string:
            string = string.replace('F', '', 1)
            string = string.replace('O', '', 1)
            string = string.replace('U', '', 1)
            string = string.replace('R', '', 1)
            num += '4'
            continue
        if 'R' in string:
            string = string.replace('T', '', 1)
            string = string.replace('H', '', 1)
            string = string.replace('R', '', 1)
            string = string.replace('E', '', 1)
            string = string.replace('E', '', 1)
            num += '3'
        if 'F' in string:
            string = string.replace('F', '', 1)
            string = string.replace('I', '', 1)
            string = string.replace('V', '', 1)
            string = string.replace('E', '', 1)
            num += '5'
            continue
        if 'O' in string:
            string = string.replace('O', '', 1)
            string = string.replace('N', '', 1)
            string = string.replace('E', '', 1)
            num += '1'
            continue
        if 'H' in string:
            string = string.replace('E', '', 1)
            string = string.replace('I', '', 1)
            string = string.replace('G', '', 1)
            string = string.replace('H', '', 1)
            string = string.replace('T', '', 1)
            num += '8'
            continue
        if 'V' in string:
            string = string.replace('S', '', 1)
            string = string.replace('E', '', 1)
            string = string.replace('V', '', 1)
            string = string.replace('E', '', 1)
            string = string.replace('N', '', 1)
            num += '7'
            continue
        if 'N' in string:
            string = string.replace('N', '', 1)
            string = string.replace('I', '', 1)
            string = string.replace('N', '', 1)
            string = string.replace('E', '', 1)
            num += '9'
            continue
    num = list(num)
    num.sort()
    return ''.join(num)


cases = int(raw_input())
for case in range(1, cases + 1):
    print "Case #{0}: {1}".format(case, solution(raw_input()))