import itertools
import sys


def iter_chunk(iterable, size):
    return zip(*([iter(iterable)] * size))


def solve(T, K, C, S):
    if K > S + C - 1:
        result = 'IMPOSSIBLE'
    else:
        combinations = itertools.combinations(range(K), min(C, K))
        final_positions = []

        for i in range(K - min(K, C) + 1):
            path = next(combinations)
            position = 1
            for i, element in enumerate(reversed(path)):
                position += K**i * element
            final_positions.append(position)

        result = ' '.join(map(str, final_positions))
    print('Case #{}: {}'.format(T, result))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for case in range(n_cases):
        K, C, S = map(int, sys.stdin.readline().strip().split(' '))
        solve(case + 1, K, C, S)


if __name__ == '__main__':
    main()
