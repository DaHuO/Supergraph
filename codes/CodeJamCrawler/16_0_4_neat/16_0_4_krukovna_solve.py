import sys


class Solved(Exception):
    pass


def solve(k, c, s):
    raise Solved(' '.join(list(map(str, range(1, k + 1)))))


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(*map(int, sys.stdin.readline().strip().split(' ')))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
