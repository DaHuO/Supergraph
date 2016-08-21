import re

patterns = {
    'E': re.compile('E'),
    'F': re.compile('F'),
    'H': re.compile('H'),
    'I': re.compile('I'),
    'N': re.compile('N'),
    'O': re.compile('O'),
    'R': re.compile('R'),
    'S': re.compile('S'),
    'T': re.compile('T'),
    'V': re.compile('V'),
    'Z': re.compile('Z')
}


digits = {
    0: [patterns['O'], patterns['R'], patterns['E'], patterns['Z']],
    1: [patterns['O'], patterns['E'], patterns['N']],
    2: [patterns['O'], patterns['T'], re.compile('W')],
    3: [patterns['T'], patterns['R'], patterns['E'], patterns['E'], patterns['H']],
    4: [patterns['F'], patterns['O'], re.compile('U'), patterns['R']],
    5: [patterns['F'], patterns['V'], patterns['I'], patterns['E']],
    6: [re.compile('X'), patterns['I'], patterns['S']],
    7: [patterns['N'], patterns['V'], patterns['S'], patterns['E'], patterns['E']],
    8: [patterns['T'], re.compile('G'), patterns['I'], patterns['E'], patterns['H']],
    9: [patterns['E'], patterns['I'], patterns['N'], patterns['N']]
}

unique_digits = {2: 'W', 4: 'U', 6: 'X', 8: 'G'}
non_unique_digits = {k: v for k, v in digits.items() if k not in unique_digits}


def find_spelling(letters, spelling):
    new_letters = letters

    for regex in spelling:
        new_string, replace_count = re.subn(regex, '', new_letters, 1)
        if replace_count == 0:
            return None
        else:
            new_letters = new_string

    return new_letters


def descramble_num(letters):
    remainder = letters
    found_nums = []
    while remainder != '':
        for digit, letter in unique_digits.items():
            #print('Checking letter {0} against remainder [{1}]'.format(letter, remainder))
            if letter in remainder:
                #print('Checking number {0} against remainder [{1}]'.format(digit, remainder))
                result = find_spelling(remainder, digits[digit])
                #print('Result is {0}'.format(result))
                while result is not None:
                    remainder = result
                    found_nums.append(digit)
                    result = find_spelling(remainder, digits[digit])
        for digit, spelling in non_unique_digits.items():
            #print('Checking number {0} against remainder [{1}]'.format(digit, remainder))
            result = find_spelling(remainder, spelling)
            #print('Result is {0}'.format(result))
            while result is not None:
                remainder = result
                found_nums.append(digit)
                result = find_spelling(remainder, spelling)
                #print('Result is {0}'.format(result))
            if remainder == '':
                break
        break
    #print('Found numbers {0}'.format(sorted(found_nums)))
    return "".join([str(n) for n in sorted(found_nums)])


def handle_file(infile):
    num_cases = int(infile.readline())
    cases = [c.strip() for c in infile.readlines()]
    answers = []

    for i in range(num_cases):
        answers.append(descramble_num(cases[i]))

    for i in range(num_cases):
        print('Case #{0}: {1}'.format(i + 1, answers[i]))


if __name__ == '__main__':
    with open("A-large.in", "r") as f:
        handle_file(f)
