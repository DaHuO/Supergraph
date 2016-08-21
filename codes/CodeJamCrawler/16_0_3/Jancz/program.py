import sys
from itertools import product
import math


def read_input(in_file):
    out_file = in_file.split('.')[0] + '.out'
    with open(in_file, 'r') as i, open(out_file, 'w') as o:
        number_of_cases = int(i.readline())
        for index in range(1, number_of_cases + 1):
            line = i.readline().strip()
            (n, j) = line.split(' ')
            result = do_algorithm(int(n), int(j))
            output = 'Case #{0}:\n'.format(index, str(result))
            for k, v in result.items():
                output += str(k) + ' ' + ' '.join(str(x) for x in v) + '\n'
            print(output)
            o.write(output)


def convert_to_base(number, base):
    if base == 10:
        return int(number)
    digits = list(number)
    digits = digits[::-1]
    converted_number = 0
    for i, d in enumerate(digits):
        converted_number += int(d) * (base ** i)
    return converted_number


def find_divisor(converted_number):
    for i in range(2, int(math.sqrt(converted_number)) + 1):
        if converted_number % i == 0:
            return i
    return None


def find_non_primes(n, j):
    decimals = {}
    numbers = product('01', repeat=n-2)
    for number_part in numbers:
        number = '1' + ''.join(number_part) + '1'
        converted_numbers_divisors = get_converted_numbers_divisors(number)
        if len(converted_numbers_divisors) == 9:
            decimals[number] = converted_numbers_divisors
        if len(decimals.keys()) == j:
            return decimals
    return {}


def get_converted_numbers_divisors(n):
    converted_numbers_divisors = []
    for i in range(2, 11):
        converted_number = convert_to_base(n, i)
        divisor = find_divisor(converted_number)
        if divisor:
            converted_numbers_divisors.append(divisor)
    return converted_numbers_divisors


def do_algorithm(n, j):
    return find_non_primes(n, j)


def generate_numbers(n):
    start_sequences = []
    for i in range(0, n - 1):
        base_string = (i * '0') + ((n - 2 - i) * '1')
        start_sequences.extend(['1' + ''.join(p) + '1' for p in permutations(base_string)])
    return list(set(start_sequences))


if __name__ == '__main__':
    read_input(sys.argv[1])
