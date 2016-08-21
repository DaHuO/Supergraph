from itertools import *
from math import *

N = 16
J = 50

prime_numbers = { }

def is_prime(rep):
    if rep in prime_numbers:
        return prime_numbers[rep]

    for divisor in xrange(2, int(sqrt(rep)) + 1):
        if rep % divisor == 0:
            prime_numbers[rep] = divisor
            break

    if rep not in prime_numbers:
        prime_numbers[rep] = True

    return prime_numbers[rep]

digits = '01'
bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in product(digits, repeat=N):
    if J == 0:
        break

    if number[0] != '1' or number[-1] != '1':
        continue

    num = ''.join(number)
    proofs = [ ]

    for i in bases:
        rep = int(num, i)
        proof = is_prime(rep)
        if proof == True:
            break
        else:
            proofs.append(str(proof))

    if len(proofs) != 9:
        continue

    output = " ".join([num] + proofs)
    print output
    J -= 1
