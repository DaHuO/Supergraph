import sympy, sympy.ntheory
from itertools import chain, cycle, accumulate # last of which is Python 3 only

with open('C-large.in', 'r') as f:
    data = f.read()

data = data.split('\n')
output = []

def factors(n):
    return sympy.ntheory.pollard_pm1(n)

def fn(n, j):
    attach_one = 2 ** (n - 1) + 1
    jamcoins = []
    for mid_bin in range(2 ** (n - 2)):
        # Check if base 2 is prime.
        num_bin = attach_one + mid_bin * 2
        if sympy.isprime(num_bin):
            continue
        num_bin = bin(num_bin)[2:]
        # Check if bases 3 - 10 are prime.
        for base in range(3, 11):
            if sympy.isprime(int(num_bin, base)):
                break
        else:
            jamcoin = num_bin
            # Find factors
            for base in range(2, 11):
                factor = factors(int(num_bin, base))
                if factor == None:
                    break
                jamcoin += ' ' + str(factors(int(num_bin, base)))
            else:
                jamcoins.append(jamcoin)
                if len(jamcoins) >= j:
                    return '\n'.join(jamcoins)

print(data.pop(0), 'cases.\n')
while data:
    if data[0] == '':
        break
    # ANSWER GOES HERE
    n, j = map(int, data.pop(0).split(' '))
    output.append(fn(n, j))

with open('submission.txt', 'w+') as f:
    i = -1
    for i, answer in enumerate(output):
        f.write("Case #%i:\n%s\n" % (i+1, answer))
        print("Case #%i:\n%s" % (i+1, answer))
    print('\n%i cases written to file' % (i+1))
