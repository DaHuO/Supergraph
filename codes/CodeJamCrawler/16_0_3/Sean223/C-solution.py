from math import sqrt

__author__ = 'sean'

OUT_FILE = "large.txt"


def try_to_get_divisor(q):
    if q <= 2:  # not composite
        return -1

    if q % 2 == 0:
        return 2

    for divisor in range(3, int(q**0.1) + 1, 2):
        if q % divisor == 0:
            return divisor

    return -1


n = 32
j = 500

output = "Case #1: \n"
number_found = 0

for candidate in range(2**(n-1), 2**n):
    if candidate % 2 == 0:
        continue  # Jam coins end with a 1

    binary_representation = bin(candidate)[2:]

    divisors = [try_to_get_divisor(int(binary_representation, base)) for base in range(2, 11)]

    if -1 not in divisors:
        number_found += 1
        output += binary_representation + ' '
        for div in divisors:
            output += str(div) + ' '
        output += '\n'

    if number_found >= j:
        break

with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
