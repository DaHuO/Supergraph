import sys
import os


def problem_specific_parser(src):
    return int(next(src))


def solve(num):
    if num == 0: return "INSOMNIA"

    digits = set([str(e) for e in range(10)])
    multiplier = 1

    while True:
        mnum = num * multiplier
        for e in str(mnum):
            digits.discard(e)

        if not digits:
            return mnum

        multiplier += 1

def parse(src):
    lines = iter(src.split(os.linesep))
    nproblems = int(next(lines))

    for problem in range(nproblems):
        yield problem_specific_parser(lines)


def main():
    src = sys.stdin.read()
    for i, data in enumerate(parse(src)):
        print("Case #{0}: {1}".format(i + 1, solve(data)))

    
if __name__ == '__main__':
    main()
