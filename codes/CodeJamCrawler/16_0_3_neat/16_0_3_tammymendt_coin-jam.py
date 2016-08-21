import sys

from math import sqrt
from itertools import count
from itertools import islice


def lowest_divisor(n):
    limit_test = 1000
    for possible_divisor in islice(count(2), int(sqrt(n) - 1)):
        if n % possible_divisor == 0:
            return possible_divisor
        limit_test -= 1
        if limit_test == 0:
            return None

    return None


def test_for_divisor(sequence, base):

    number = int(sequence, base)
    return lowest_divisor(number)


def test_jam_coin(sequence):
    print sequence
    result = []
    for base in range(2, 11):
        d = test_for_divisor(sequence, base)
        if d:
            result.append(d)
        else:
            return False
    return result


def generate_jam_coins(n, j):
    max_number = 2**n - 1
    min_number = 2**(n-2)
    i = 0

    while min_number + i < max_number:
        sequence = str(bin(min_number + i)).replace('0b', '') + '1'
        divisors = test_jam_coin(sequence)
        if divisors:
            yield sequence, divisors
        i += 1


def main():

    out_file = open('out.txt', 'w')
    in_file = open(sys.argv[1], 'r')
    in_file.readline()
    input = in_file.readline().split(' ')
    n = int(input[0])
    j = int(input[1])

    jam_coins = generate_jam_coins(n, j)
    out_file.write('Case #1:\n')

    i = 0
    while i < j:
        jam_coin = jam_coins.next()
        sequence = jam_coin[0]
        divisors = jam_coin[1]
        out_file.write('%s %s\n' % (sequence, ' '.join(map(str, divisors))))
        i += 1


if __name__ == "__main__":

    main()
