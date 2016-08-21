
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')

import math
N = 10000000

seive = [True] * (N)
seive[0] = seive[1] = False

rt = int(math.sqrt(N))+1
for p in range(2, rt):
    if seive[p]:
        seive[p*p:N:p] = [False]* ( len(seive[p*p::p]) )

primes = {}

print 'seivi init'

def is_prime1(k):
    if k in primes:
        return True

    for i in xrange(2, k//2+1):
        if k%i == 0:
            return False

    primes[k] = True

    # print 'p' , k, seive[k]
    # return seive[k]

    return True

def is_prime(k):
    if k > N:
        return is_prime1(k)

    return seive[k]

def get_candidate(n):
    c = 1
    p = pow(2, n-1)

    while (p+c) != (pow(2, n)+1):
        yield p + c
        c += 2


def get_base(n, b):
    in_bin = bin(n).replace('0b', '')
    return int(in_bin, b)

def is_jamcoin(n):
    if is_prime(n):
        return False

    for i in xrange(2, 10):
        if is_prime( get_base(n, i) ):
            # print 'f', i, n, bin(n), get_base(n, i)
            return False

    return True

def get_a_div(n):
    # if is_prime(n):
    #     return False

    if n % 2 == 0:
        return 2
    else:
        i = 3
        while i*i < n:
            if n%i == 0:
                return i

            i += 2

    return False


def get_jam_divisors(n):
    divs = []
    for i in xrange(2, 11):
        value = get_base(n, i)
        print value
        value = get_a_div(value)
        if not value:
            return []

        divs.append( str(value) )

    return divs

case = 0
for a_input in input_lines[1:]:
    case += 1

    N, J = map(int, a_input.split(' '))

    value = get_candidate(N)
    jam = []
    # print get_base(55, 3)
    # print is_jamcoin(35)

    # print get_jam_divisors(32785)

    c = 1
    p = pow(2, N-1)

    while (p+c) != (pow(2, N)+1):
        jam.append(p+c)
        if len(jam) == 100:
            break
        c += 2

    print jam

    output_jams = []
    for a_jam in jam:
        print a_jam
        divisors = get_jam_divisors(a_jam)
        if divisors:
            output_jams.append([a_jam, divisors])

        if len(output_jams) == J:
            break

    # print output_jams

    value = '\n'
    for a_jam, divisors in output_jams:
        value += str(bin(a_jam).replace('0b', '')) + ' ' + ' '.join(divisors) + '\n'

    # value = 0
    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)