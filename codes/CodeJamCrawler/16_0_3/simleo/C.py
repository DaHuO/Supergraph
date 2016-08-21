import sys
import argparse
from random import randint


def read_input(f):
    N = int(f.next())
    assert N == 1
    return map(int, f.next().split())


def gen_coin(N):
    return '1%s1' % ''.join(map(str, [randint(0, 1) for _ in xrange(N - 2)]))


def factorize(n):
    primes = []
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            primes.append(i)
            n = q
        else:
            i += 1
    primes.append(n)
    return primes


def make_random_jc(N):
    coin = gen_coin(N)
    divisors = []
    for base in xrange(2, 11):
        factors = factorize(int(coin, base))
        if len(factors) < 2:
            raise ValueError
        divisors.append(factors[-1])
    return coin, divisors


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", '--in_', metavar="FILE", help="input file")
    parser.add_argument("-o", "--out", metavar="FILE", help="output file")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    if args.in_ is None:
        args.in_ = sys.stdin
    else:
        args.in_ = open(args.in_)
    if args.out is None:
        args.out = sys.stdout
    else:
        args.out = open(args.out, "w")
    N, J = read_input(args.in_)
    args.out.write("Case #1:\n")
    gen = set()
    while len(gen) < J:
        try:
            coin, divisors = make_random_jc(N)
        except ValueError:
            pass
        else:
            if coin not in gen:
                args.out.write(
                    "%s %s\n" % (coin, " ".join(map(str, divisors)))
                )
                gen.add(coin)


if __name__ == "__main__":
    main(sys.argv)
