import os
import re
import sys


numbers = {'SIX': 6,
           'ZERO': 0,
           'FOUR': 4,
           'TWO': 2,
           'ONE': 1,
           'THREE': 3,
           'FIVE': 5,
           'SEVEN': 7,
           'EIGHT': 8,
           'NINE': 9}

number_list = ['SIX', 'ZERO', 'FOUR', 'TWO', 'ONE', 'THREE', 'FIVE', 'SEVEN', 'EIGHT', 'NINE']


def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def task(S):
    chars = list(S)
    result = []
    for number in number_list:
        while True:
            positions = []
            for i, c in enumerate(list(number)):
                for cp in findOccurences(chars, c):
                    if cp not in positions:
                        positions.append(cp)
                        #print('append (%s): %d' % (c, chars.index(c)))
                        break
            if len(positions) == len(number):
                result.append(numbers[number])
                for p in positions:
                    chars[p] = '-'
                #print(chars)
            else:
                break
            #print(result)
        #break
    #print(result)
    result.sort()
    assert ''.join(chars) == ''.join(len(chars) * '-'), '%s - %s' % (S, ''.join(map(str, result)))
    return ''.join(map(str, result))


def main():
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()

    T = int(lines[0])
    res = ''
    for i in range(1, T + 1):
        res += 'Case #%d: %s\n' % (i, task(lines[i]))

    with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as f:
        f.write(res)

if __name__ == '__main__':
    main()
