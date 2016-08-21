"""

@author: Nishant Kumar
Date: 30-04-2016

"""

__author__ = 'Nishant Kumar'

from collections import defaultdict
import os

def get_number(s):
    chars = defaultdict()
    for ch in s:
        chars.setdefault(ch, 0)
        chars[ch] += 1

    numbers = []

    # 0
    if chars.get('Z', 0) > 0:
        no = chars['Z']
        chars['Z'] -= no
        chars['E'] -= no
        chars['R'] -= no
        chars['O'] -= no
        numbers.append('0' * no)
    # 2
    if chars.get('W', 0) > 0:
        no = chars['W']
        chars['T'] -= no
        chars['W'] -= no
        chars['O'] -= no
        numbers.append('2' * no)
    # 4
    if chars.get('U', 0) > 0:
        no = chars['U']
        chars['F'] -= no
        chars['O'] -= no
        chars['U'] -= no
        chars['R'] -= no
        numbers.append('4' * no)

    # 6
    if chars.get('X', 0) > 0:
        no = chars['X']
        chars['S'] -= no
        chars['I'] -= no
        chars['X'] -= no
        numbers.append('6' * no)

    # 7
    if chars.get('S', 0) > 0:
        no = chars['S']
        chars['S'] -= no
        chars['E'] -= no
        chars['V'] -= no
        chars['E'] -= no
        chars['N'] -= no
        numbers.append('7' * no)

    # 1
    if chars.get('O', 0) > 0:
        no = chars['O']
        chars['O'] -= no
        chars['N'] -= no
        chars['E'] -= no
        numbers.append('1' * no)

    # 5
    if chars.get('V', 0) > 0:
        no = chars['V']
        chars['F'] -= no
        chars['I'] -= no
        chars['V'] -= no
        chars['E'] -= no
        numbers.append('5' * no)

    # 3
    if chars.get('R', 0) > 0:
        no = chars['R']
        chars['T'] -= no
        chars['H'] -= no
        chars['R'] -= no
        chars['E'] -= 2 * no
        numbers.append('3' * no)

    # 8
    if chars.get('H', 0) > 0:
        no = chars['H']
        chars['E'] -= no
        chars['I'] -= no
        chars['G'] -= no
        chars['H'] -= no
        chars['T'] -= no
        numbers.append('8' * no)

    # 9
    if chars.get('I', 0) > 0:
        no = chars['I']
        chars['N'] -= no
        chars['I'] -= no
        chars['N'] -= no
        chars['E'] -= no
        numbers.append('9' * no)

    phone = ''
    for num in sorted(numbers):
        phone += num

    for ch in chars:
        if chars[ch] != 0:
            print (s, phone, chars)
    return phone


def main():
    home_dir = r'C:\Users\Nishant\Dropbox\CodeBase\Coding Competitions\GoogleCodeJam_2016\Round_1B'

    input_file  = os.path.join(home_dir, 'A-large.in')
    output_file = os.path.join(home_dir, 'A-large.out')

    f = open(input_file, 'r')
    o = open(output_file, 'w')

    total_cases = int(f.readline())
    inputs = list(f)
    case_no = 1

    while case_no <= total_cases:
        string = inputs[case_no-1].strip()
        o.write ("Case #%s: %s\n" %(case_no, get_number(string)))
        case_no += 1

    f.close()
    o.close()

if __name__ == '__main__':
    main()