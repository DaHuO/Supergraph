import sys
import argparse
from string import uppercase
from collections import Counter


def read_input(f):
    N = int(f.next())
    for i in xrange(N):
        f.next()
        yield i, map(int, f.next().split())


def check_plan(plan, c):
    for step in plan:
        for p in step:
            assert p in c
            c[p] -= 1
        if c:
            assert c.most_common(1)[0][1] <= sum(c.itervalues()) // 2


def solve(case):
    c = Counter()
    c.update(dict(zip(uppercase, case)))
    plan = []
    while True:
        if not c:
            break
        if len(c) == 3 and sum(c.itervalues()) == 3:
            plan.append(c.popitem()[0])
            continue
        mc = c.most_common(2)
        (p1, count1), (p2, count2) = mc
        if count1 - count2 > 1:
            plan.append(2 * p1)
            c[p1] -= 2
        else:
            plan.append(p1 + p2)
            c[p1] -= 1
            c[p2] -= 1
        if c[p1] <= 0:
            del c[p1]
        if c[p2] <= 0:
            del c[p2]
    check_plan(plan, Counter(dict(zip(uppercase, case))))
    return plan


def write_result(idx, res, fo):
    fo.write("Case #%d: %s\n" % (idx + 1, " ".join(res)))


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
