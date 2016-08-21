"""
    Oh yeah baby
"""
from itertools import product

def find_jamcoins(n, j):
    divisor_list_list = []
    found_j = 0
    for try_string in product('01', repeat = n-2):
        candidate = '1' + ''.join(try_string) + '1'
        result = is_jamcoin(candidate)
        if result:
            found_j += 1
            divisor_list_list = divisor_list_list + [[candidate, result]]
        if found_j == j:
            return divisor_list_list


def is_jamcoin(in_string):
    divisors = []
    for b in range(2,11):
        num = int(in_string, b)
        found_div = False
        max_range = min(100000, num-1)
        for i in range(2, max_range):
            if num % i == 0:
                divisors = divisors + [i]
                found_div = True
                break
        if found_div == False:
            return False
    return divisors

with open('input.in') as ifile:
    with open('output.out', 'w') as ofile:
        ifile.readline()
        i = 1
        for line in ifile:
            inputs = line.split(' ')
            result_list = find_jamcoins(int(inputs[0]), int(inputs[1]))
            ofile.write('Case #{}:\n'.format(i))
            for result in result_list:
                jamstring = result[0]
                divisors = [str(div) for div in result[1]]
                ofile.write('{} {}\n'.format(jamstring, ' '.join(divisors)))
            i += 1
