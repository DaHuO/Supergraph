import pyprimes # pip install pyprimes or https://pypi.python.org/pypi/pyprimes/
from pyprimes import isprime

min_length = 16
examples = 50

base = [0]*min_length
base[0] = 1
base[-1] = 1

output_file = open('ASmall.out', 'w')
output_file.write('Case #1:\n')

while examples > 0:

    prime_fail = False
    divisors = []

    for i in xrange(2,11):
        value = 0
        for j in xrange(0,len(base)):
            value += pow(i,j)*base[j]
        if isprime(value):
            prime_fail = True
            break
        else:
            # find divisor
            it = pyprimes.primes()
            divisor = next(it)
            while not ((value % divisor) == 0):
                divisor = next(it)
            divisors.append(divisor)

    if not prime_fail:
        string = ('example %d: ' % (51 - examples))
        string = ''
        for i in xrange(0,len(base)):
            ms = base[len(base)-1-i]
            string += str(ms)
        for divisor in divisors:
            string += (' %d' % divisor)
        print(string)
        output_file.write(string+'\n')
        examples += -1

    base[1] += 1
    for x in range(1, len(base)-1):
        if base[x] == 2:
            base[x] = 0
            base[x+1] += 1
    if not base[len(base)-1] == 1:
        base[-1] = 1

output_file.close()