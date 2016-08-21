import sys
import argparse
import string


ALL_DIGITS = frozenset(string.digits)


def read_input(f):
    N = int(f.next())
    for i in xrange(N):
        yield i, int(f.next().strip())


def solve(n):
    digits = set()
    if n <= 0:
        return None
    i = 1
    while True:
        if digits == ALL_DIGITS:
            return n * (i - 1)
        digits.update(str(n * i))
        i += 1


def write_result(idx, res, fo):
    if res is None:
        res = "INSOMNIA"
    fo.write("Case #%d: %s\n" % (idx + 1, res))


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
        args.out = open(args.out)
    for i, case in read_input(args.in_):
        write_result(i, solve(case), args.out)


if __name__ == "__main__":
    main(sys.argv)
