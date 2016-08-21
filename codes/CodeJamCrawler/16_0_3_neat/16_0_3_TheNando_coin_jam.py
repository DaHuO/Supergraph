import sys
import random


SYMBOLS = '0123456789'
EVEN_NUMBERS = {0, 2, 4, 6, 8}


def read_input(filename, operation=lambda x: x):
    with open(filename, 'r') as f:
        return (operation(item) for item in f.readlines())


def write_results(results, filename):
    with open(filename, 'w') as f:
        f.writelines(results)


def naive_non_prime(number):
    last_digit = int(str(number)[-1])
    if last_digit in EVEN_NUMBERS:
        return 2

    if last_digit == 5:
        return 5

    if number % 3 == 0:
        return 3

    if number % 7 == 0:
        return 7

    if number % 9 == 0:
        return 9

    return False


def get_divisor(number):
    pass


def verify_non_prime_bases(jamcoin):
    divisors = []
    for base in range(2, 11):
        test = int(jamcoin, base)
        divisor = naive_non_prime(test)
        if not divisor:
            return False
        divisors.append(divisor)
    return divisors


def generate_potential_jamcoin(length):
    rand = random.getrandbits(length - 2)
    return '1' + '{0:b}'.format(rand).zfill(length - 2) + '1'


def collect_jamcoins(size, count):
    jamcoins = {}

    while len(jamcoins) < count:
        jc = generate_potential_jamcoin(size)
        divisors = verify_non_prime_bases(jc)
        if divisors:
            jamcoins[jc] = divisors

    return jamcoins


# get script name
name = sys.argv[0].split('/').pop().split('.')[0]

# read trials from script input file and strip each line
trials = read_input('{}.in'.format(name), lambda x: x.rstrip())

# first line is number of trials, which isn't needed
next(trials)

(count, size) = next(trials).split(' ')
count = int(count)
size = int(size)

# run trials and collect results
data = collect_jamcoins(count, size)

# create output strings from results
output = ['Case #1:\n']
for key, value in data.items():
    output.append('{} {}\n'.format(key, ' '.join(str(v) for v in value)))

print(output)

# write output
write_results(output, '{}.out'.format(name))
