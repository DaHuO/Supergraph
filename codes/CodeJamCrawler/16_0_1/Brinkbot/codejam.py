import sys
import itertools


def parse_and_solve(inp):
    num = int(next(inp))
    if num == 0:
        return 'INSOMNIA'
    else:
        present = [False] * 10
        for i in itertools.count(1):
            mult = num * i
            for ind in map(int, str(mult)):
                present[ind] = True
            if all(present):
                return str(mult)


def main():
    num = int(next(sys.stdin))
    for i in range(1, num + 1):
        sys.stdout.write('Case #{:d}: {}\n'.format(
            i, parse_and_solve(sys.stdin)))


if __name__ == '__main__':
    main()
