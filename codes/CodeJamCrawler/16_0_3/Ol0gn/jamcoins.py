__author__ = 'sumant'


from itertools import count, islice

# cache atleast some values
known_primes = []

def check_is_prime(num):
    for prime in known_primes:
        if num % prime == 0:
            return prime
    # Returns 0 if prime, otherwise returns a divisor
    sqrt = num ** 0.5
    for i in islice(count(2), known_primes[-1] + 1, int(sqrt)):
        if i > sqrt:
            break
        if num % i == 0:
            return i


def get_jamcoins_with_proof(n, num_coins):
    coins_found = 0
    num_str = ''.join(['0' for _x in range(n-2)])
    num_str = '1' + num_str + '1'
    ret = {}
    while coins_found < num_coins:
        is_prime = False
        divisors = []
        num_b2 = 0
        for base in range(2, 11):
            num = int(num_str, base)
            if base == 2:
                num_b2 = num
            div = check_is_prime(num)
            if div == 0:
                is_prime = True
                break
            divisors.append(div)
        if not is_prime:
            ret[num_str] = divisors
            coins_found += 1
        num_b2 += 2
        num_str = bin(num_b2)[2:]
    return ret


if __name__ == '__main__':
    with open('primes_sm', 'rb') as fp:
        known_primes = map(int, fp.readlines()[0].strip().split(','))

    n = int(raw_input())
    for i in range(n):
        n, j = map(int, str(raw_input()).split())
        print 'Case #%s:' % (i+1)
        ret = get_jamcoins_with_proof(n, j)
        for k, v in ret.iteritems():
            print '%s %s' % (k, ' '.join([str(_x) for _x in v]))