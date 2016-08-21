import sys
import re


def is_prime(number):
    return number < 100000 and re.match(r'^1?$|^(11+?)\1+$', '1' * number) is None


def find_factor(number):
    for i in range(2, number):
        if i > 1000:
            break
        if number % i == 0:
            return i
    return None


def gen_jamcoin(gen_counter, n):
    gen_counter += 1
    jamcoin = '1{0}1'.format(format(gen_counter, '0{0}b'.format(n - 2)))
    return gen_counter, jamcoin


def gen_divisors(jamcoin):
    factors = []
    for i in range(2, 11):
        base_int = int(jamcoin, i)
        factor = find_factor(base_int)
        if factor:
            factors.append(str(factor))
        else:
            return None
    return factors


def get_results(n, j):
    gen_counter = 0
    j_counter = 0
    results = []
    while j_counter < j:
        gen_counter, jamcoin = gen_jamcoin(gen_counter, n)
        factors = gen_divisors(jamcoin)
        if factors:
            result = [jamcoin]
            result.extend(factors)
            results.append(result)
            j_counter += 1

            out_file.write('{0}\n'.format(' '.join(result)))
    return results


filename = sys.argv[1]
t_array = []
out_file = open(filename.replace('in', 'out'), 'w')
with open(filename, 'r') as in_file:
    for line in in_file:
        line = line.rstrip('\n').split(' ')
        t_array.append(line)
        if len(t_array) > 1:
            out_file.write("Case #{0}:\n".format(len(t_array) - 1))
            results = get_results(int(line[0]), int(line[1]))
