import os, sys

def rem(s,sub):
    for e in sub:
        s.remove(e)

def solve_case(input_data):
    print(input_data)
    s = list(input_data)
    digits = []
    while len(s) > 0:
        if 'Z' in s:
            digits.append(0)
            rem(s, list('ZERO'))
        elif 'W' in s:
            digits.append(2)
            rem(s,(list('TWO')))
        elif 'X' in s:
            digits.append(6)
            rem(s,(list('SIX')))
        elif 'G' in s:
            digits.append(8)
            rem(s,(list('EIGHT')))
        elif 'H' in s:
            digits.append(3)
            rem(s, list('THREE'))
        elif 'R' in s:
            digits.append(4)
            rem(s,list('FOUR'))
        elif 'O' in s:
            digits.append(1)
            rem(s,list('ONE'))
        elif 'F' in s:
            digits.append(5)
            rem(s,list('FIVE'))
        elif 'V' in s:
            digits.append(7)
            rem(s,list('SEVEN'))
        else:
            digits.append(9)
            rem(s,list('NINE'))
        print(s)
    return ''.join(map(str, sorted(digits)))



if __name__ == '__main__':
    #path = './A-small-attempt0.in'
    path = './A-large.in'
    out = open(path + '.out', 'w', newline='')
    count = 1
    with open(path) as f:
        f.readline()
        for case in f:
            out.write("Case #%i: %s\n" % (count, solve_case(case.strip())))
            count += 1
    out.close()
    print('done')
