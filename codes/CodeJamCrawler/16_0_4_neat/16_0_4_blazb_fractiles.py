import sys
import os


def problem_specific_parser(src):
    return [int(e) for e in next(src).split(' ')]


def solve(data):
    K, C, S = data

    elements = [e + 1 for e in range(K)]
    offset = K
    for _ in range(1, C):
        elements = [e + idx * offset for idx, e in enumerate(elements)]
        offset *= K

    return ' '.join([str(e) for e in elements])


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
