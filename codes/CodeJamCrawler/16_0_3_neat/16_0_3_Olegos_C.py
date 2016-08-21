import math


def to_base(s, base):
    if s[-1] == '\n':
        s = s[:-1]
    pos = len(s) - 1
    power = 0
    result = 0
    while pos >= 0:
        result += int(s[pos]) * pow(base, power)
        pos -= 1
        power += 1
    return result


def get_divider(n):
    for result in range(int(math.sqrt(n)) + 1)[2:]:
        if n % result == 0:
            return result
    return 0


def get_coins(J, N):
    result = []
    count = 0
    number = pow(2, N - 1) + 1
    while count < J:
        print('count: {}'.format(count))
        b = bin(number)[2:]
        r = [b]
        for base in range(2, 11):
            n = to_base(b, base)
            d = get_divider(n)
            r.append(str(d))
        if '0' not in r:
            result.append(r)
            count += 1
        number += 2
    return result


input_file = open('in.txt', 'r')
lines = []
for l in input_file:
    lines.append(l)
numbers = lines[-1].split(' ')
print('lines: {}, numbers: {}'.format(lines, numbers))
N = int(numbers[0])
J = int(numbers[1])
output_file = open('out.txt', 'w')
output_file.write('Case #1:\n')

coins = get_coins(J, N)
for c in coins:
    output_file.write('{}\n'.format(' '.join(c)))
output_file.close()
