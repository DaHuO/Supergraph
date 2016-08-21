# Used this for prime numbers:
# http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
import sys
import funcy

#stdin = sys.stdin
#num_cases = int(stdin.readline())
#
#def parse_and_solve_case():
#    pancake_sequence = stdin.readline()
#    print pancake_sequence
#    return find_cost(pancake_sequence.strip())
#
#for case in range(num_cases):
#    print case
#    output = parse_and_solve_case()
#    print 'case #{}: {}'.format(case+1, output)

@funcy.memoize
def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def get_divisor(num):
    if is_prime(num):
        return None
    for i in xrange(2, num):
        if num % i  == 0:
            return i

def generate_test_coin(n):
    """n is sequence"""
    for i in range(2**(n-2)):
        sequence = '1' + bin(i)[2:].zfill(n-2) + '1'
        yield sequence

def get_divisors_for_test_coin(coin_sequence):
    bases = range(2, 11)
    divisors = []
    for base in bases:
        test_number = int(coin_sequence, base)
        divisor = get_divisor(test_number)
        if divisor:
            divisors.append(divisor)
        else:
            return None
    return divisors


def solve(n, j):
    num_coins = 0
    for test_coin in generate_test_coin(n):
        divisors = get_divisors_for_test_coin(test_coin)
        if divisors:
            num_coins += 1
            divisors = ' '.join(map(str, divisors))
            print '{} {}'.format(test_coin, divisors)

        if num_coins >= j:
            break

print 'Case #{}:'.format(1)
solve(16, 50)


