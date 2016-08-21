from collections import Counter

digits = {
    1: Counter('ONE'),
    2: Counter('TWO'),
    3: Counter('THREE'),
    4: Counter('FOUR'),
    5: Counter('FIVE'),
    6: Counter('SIX'),
    7: Counter('SEVEN'),
    8: Counter('EIGHT'),
    9: Counter('NINE'),
    0: Counter('ZERO')
}

first = {
    0: 'Z',
    2: 'W',
    4: 'U',
    6: 'X',
    8: 'G',
}

second = {
    3: 'H',
    5: 'F',
}

third = {
    1: 'O',
    7: 'V'
}

fourth = {
    9: 'I'
}

groups = [first, second, third, fourth]

def find_number(ch_counter):
    found_digits = []
    for group in groups:
        for digit, unique_ch in group.items():
            ch_count = ch_counter[unique_ch]
            for _ in xrange(ch_count):
                ch_counter -= digits[digit]
                found_digits.append(digit)
    return sorted(found_digits)

            

if __name__ == '__main__':
    with open('big_a.in') as fd:
        numbers = [Counter(line.strip()) for line in fd]
        numbers = numbers[1:]


    found_numbers = map(find_number, numbers)
    output_str = map(lambda case: ''.join(map(str, case)), found_numbers)

    with open('output_big.txt', 'w') as fd:
        for idx, case in enumerate(output_str):
            fd.write('Case #{}: {}\n'.format(idx+1, case))
