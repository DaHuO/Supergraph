import sys
import collections

Case = collections.namedtuple("Case", ["k", "c", "s"])


def parse_file(fname):
    with open(fname, "r") as fh:
        lines = fh.readlines()[1:]

    return [Case(*map(int, line.strip().split())) for line in lines]


def answer(case):
    checks = []
    for i in range(case.k):
        offset = 0
        for exp in range(case.c):
            offset += i*(case.k**exp)

        checks.append(offset+1)

    return " ".join([str(c) for c in checks])


def main():
    fname = sys.argv[1]
    outname = sys.argv[2]

    ns = parse_file(fname)

    answers = [answer(n) for n in ns]

    with open(outname, "w") as fh:
        for i, a in enumerate(answers, 1):
            fh.write("Case #%i: %s\n" % (i, a))

if __name__ == "__main__":
    main()
