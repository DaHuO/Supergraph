# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * int(n / 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * i / 2)::i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, int(n / 2)) if sieve[i]]


primes = primes1(int('1' * 6))


def find_divisor(a):
    for prime in primes:
        if prime >= a:
            break
        if not a % prime:
            return prime
    return 0


def is_coin_jam(s):
    divisors = list()
    for base in range(2, 10 + 1):
        value = int(s, base=base)
        divisor = find_divisor(value)
        if not divisor:
            return False
        divisors.append(int(divisor))
    print('{0} {1}'.format(s, ' '.join(map(str, divisors))))
    return True


def solve(N, J):
    inner_jam = '1' + '0' * (N - 2) + '1'
    while J > 0:
        if is_coin_jam(inner_jam):
            J -= 1
        inner_jam = '{0:b}'.format(int(inner_jam, 2) + 2)
    pass


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()

    T = int(f.readline())
    for t in range(1, T + 1):
        N, J = map(int, f.readline().split())
        print("Case #%i:" % (t,))
        solve(N, J)
