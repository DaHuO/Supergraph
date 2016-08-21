import sys, itertools

def read_primes(fname):
    with open(fname) as f:
        content = f.readlines()

    return map(int, content)

def get_divisor(n):
    global primes

    for prime in primes:
        if prime >= n:
            return False

        if n % prime == 0:
            return prime

    return False

def is_jamcoin(n, bases):
    divisors = [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for base in bases:
        basen_val = int(n, base)

        divisor = get_divisor(basen_val)
        if divisor:
            divisors[base] = divisor
        else:
            return False

    print n,
    for divisor in divisors[2:]:
        print '%d' % divisor,
    print
    return True


def main():
    global primes

    T = int(raw_input())
    (N, J) = map(int, raw_input().split())
    primes = read_primes(sys.argv[1])

    c = 0
    bases = range(2, 11)

    print 'Case #1:'

    lower_limit = '1' + '0'*(N-2) + '1'
    upper_limit = '1'*N

    lower_limit_b10 = int(lower_limit, 2)
    upper_limit_b10 = int(upper_limit, 2)

    for x in xrange(lower_limit_b10, upper_limit_b10+1):
        n = '{0:b}'.format(x)
        if n[0] == '1' and n[-1] == '1' and is_jamcoin(n, bases):
            c += 1
            if c == J:
                break

    # for x in map(''.join, itertools.product('01', repeat = N-2)):
    #     n = '1' + x + '1'
    #     if is_jamcoin(n, bases):
    #         c += 1
    #         if c == J:
    #             break


if __name__ == "__main__":
    main()

primes = []