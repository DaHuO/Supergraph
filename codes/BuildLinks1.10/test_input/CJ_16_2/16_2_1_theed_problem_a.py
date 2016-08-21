import sys
from collections import OrderedDict


def sheep(number):
    unique = OrderedDict()
    unique['Z'] ='0'
    unique['W'] ='2'
    unique['G'] ='8'
    unique['X'] ='6'
    unique['H'] ='3'
    unique['U'] ='4'
    unique['F'] ='5'
    unique['V'] ='7'
    unique['O'] ='1'
    unique['N'] ='9'

    nums = {
        '0': "ZERO",
        '1': "ONE",
        '2': "TWO",
        '3': "THREE",
        '4': "FOUR",
        '5': "FIVE",
        '6': "SIX",
        '7': "SEVEN",
        '8': "EIGHT",
        '9': "NINE"
    }
    result = []
    for i in unique:
        n = unique[i]
        while i in number:
            for c in nums[n]:
                number = number.replace(c, '', 1)
            result.append(n)
    result.sort()
    return "".join(result)


def main():
    name = sys.argv[1]
    with open(name, 'r') as f:
        content = f.read()
    lines = content.splitlines()
    num = lines[0]
    result = ''
    for n in range(int(num)):
        case = lines[1 + n]
        result += 'Case #{}: {}\n'.format(1 + n, sheep(case))
    with open(name.replace('in', 'sol'), 'w') as f:
        f.write(result)


def test():
    cases = {
        'OZONETOWER': '012',
        'WEIGHFOXTOURIST': '2468',
        'OURNEONFOE': '114',
        'ETHER': '3',
    }
    for inp, expected in cases.items():
        actual = sheep(inp)
        assert actual == expected, 'Got {}, expected {} on {}'.format(actual, expected, inp)


if __name__ == '__main__':
    main()
