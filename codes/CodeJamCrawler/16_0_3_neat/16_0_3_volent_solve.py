import math


def from_base(jamcoin, base):
    """
    Convert a jamcoin in a given base
    """
    result = 0
    i = 0
    jamcoin = map(int, jamcoin)

    while jamcoin:
        result += jamcoin.pop() * (base ** i)
        i += 1

    return result


def left_pad(coin, size, pad='0'):
    return pad * (size - len(coin)) + coin


def gen_jamcoins(size):
    for x in xrange(from_base([1] * (size - 2), 2) + 1):
        yield '1' + left_pad(bin(x)[2:], size - 2) + '1'


def is_prime(n):
    if n <= 3:
        return True

    if n % 2 == 0:
        return 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    return True


def has_any_prime(jamcoin):
    divisors = []

    for base in range(2, 11):
        divisor = is_prime(from_base(jamcoin, base))
        if divisor is True:
            return None
        divisors.append(divisor)

    return divisors


def solve(N, J):
    for jamcoin in gen_jamcoins(N):
        divisors = has_any_prime(jamcoin)
        if divisors is not None:
            print ' '.join(map(str, [jamcoin] + divisors))
            J -= 1
        if J <= 0:
            break


def main():
    T = input()
    for N in xrange(T):
        print "Case #{}:".format(N + 1)
        solve(*map(int, raw_input().split()))

if __name__ == "__main__":
    main()
