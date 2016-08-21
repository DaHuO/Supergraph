import random

THRESHOLD = 5000

def generate_potential_jamcoin(n):
    middle = ''.join([random.sample(['0', '1'], 1)[0] for x in range(n - 2)])
    return '1' + middle + '1'

def is_jamcoin(str):
    """For speed, just tests the primality."""
    for base in range(2, 11):
        to_test = int(str, base)
        if is_prime(to_test):
            return False
    return True

def generate_jamcoin(n, j):
    solns = []
    while True:
        potential_jamcoin = generate_potential_jamcoin(n)
        if is_jamcoin(potential_jamcoin):
            solns.append(potential_jamcoin)
            if len(solns) == j:
                return solns

def get_jamcoin_factors(jamcoin):
    factors = []
    for base in range(2, 11):
        num = int(jamcoin, base)
        factors.append(get_nontrivial_factor(num))
    return [str(factor) for factor in factors]


def is_prime(x):
    c = 0
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            c += 1
            if c > THRESHOLD:
                return True
            if x % i == 0:
                return False
        return True
    else:
        return False

def get_nontrivial_factor(x):
    for i in range(2, x):
        if x % i == 0:
            return i
    raise Exception()

if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    n, j = map(int, input().split(' '))

    jamcoins = generate_jamcoin(n, j)
    while len(jamcoins) != len(set(jamcoins)):
        jamcoins = generate_jamcoin(n, j)

    print("Case #1:")
    for jamcoin in jamcoins:
        print(' '.join([jamcoin] + get_jamcoin_factors(jamcoin)))
