import itertools
import collections

def get_nontrivial_divisor(n):
    for i in range(2, 11):
        if n%i == 0:
            return i
    return 0

def solution(length, count):
    bases = [base**length for base in range(2, 11)]
    jamcoins = []
    primes = []
    for binary in itertools.product(['0', '1'], repeat=length-2):
        if len(jamcoins) == count:
            break
        binary = '1' + ''.join(binary) + '1' 
        divisors = []
        for base in range(2, 11):
            number = int(binary, base)
            divisor = get_nontrivial_divisor(number)
            if not divisor:
                break
            else:
                divisors.append(divisor)
        else:
            divisors = ' '.join([str(elem) for elem in divisors])
            jamcoins.append((binary, divisors))
    return jamcoins

with open('input', 'r') as infile, open('output', 'w') as out:
    next(infile)
    line = next(infile).split()
    length, count = int(line[0]), int(line[1])
    out.write("Case #1:\n")
    for binary, divisors in solution(length, count):
        out.write("{0} {1}\n".format(binary, divisors))
