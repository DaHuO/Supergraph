import sys

import math


def digits_to_number(digits, base):
    number = 0
    for d in digits:
        number = base * number + int(d)
    return number


def nontrivial_divisors(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i


def generate_jamcoin_candidate(hash, length):
    bin_hash = bin(hash)[2:]
    zero_prefix = '0' * (length - 2 - len(bin_hash))
    return '1{}{}1'.format(zero_prefix, bin_hash)


def find_jamcoin_divs(jamcoin):
    divs = {}
    for base in range(2, 11):
        number = digits_to_number(list(jamcoin), base)
        div = next(nontrivial_divisors(number), -1)
        if div < 0:
            return None
        divs['base{}div'.format(base)] = div
    return divs


def generate_jamcoins(length, count):
    jamcoins = []
    hash = 0
    while len(jamcoins) < count:
        candidate = generate_jamcoin_candidate(hash, length)
        divs = find_jamcoin_divs(candidate)
        if divs:
            divs['value'] = candidate
            jamcoins.append(divs)
            print('{} jamcoins'.format(len(jamcoins)))
        hash += 1
    return jamcoins


def main():
    task_input = open(sys.argv[1], 'r')
    task_output = open(sys.argv[1] + '.out', 'w')
    cases_count = int(task_input.readline())
    for case in range(1, cases_count + 1):
        case_strings = task_input.readline().rstrip().split(' ')
        length = int(case_strings[0])
        count = int(case_strings[1])
        jamcoins = generate_jamcoins(length, count)
        task_output.write('Case #{}:\n'.format(case))
        for jamcoin in jamcoins:
            task_output.write(jamcoin['value'])
            for base in range(2, 11):
                task_output.write(' {}'.format(jamcoin['base{}div'.format(base)]))
            task_output.write('\n')
    task_input.close()
    task_output.close()


main()
