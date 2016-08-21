import sys
import argparse


def read_input(f):
    N = int(f.next())
    for i in xrange(N):
        yield i, f.next().strip()


def flip(s, n):
    seq = [1 if _ == '+' else 0 for _ in s]
    for i in xrange(n):
        seq[i] ^= 1
    return ''.join('+' if _ else '-' for _ in seq)


def solve(s):
    moves = 0
    while True:
        try:
            n = s.rindex('-')
        except ValueError:
            return moves
        else:
            s = flip(s, n+1)
            moves += 1


def write_result(idx, res, fo):
    fo.write("Case #%d: %d\n" % (idx + 1, res))


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
