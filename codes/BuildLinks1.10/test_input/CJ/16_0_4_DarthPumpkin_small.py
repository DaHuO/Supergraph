# http://www.numpy.org/
import numpy as np

def solve(k, c):
    a = np.arange(1, k + 1)
    b = a.copy()
    for e in range(1, c):
        b += (a - 1) * k ** e
    return b


def main():
    T = int(raw_input())
    test_cases = [map(int, raw_input().split(' ')) for _ in range(T)]
    for i, (k, c, _) in enumerate(test_cases):
        print 'Case #{}: {}'.format(i + 1, ' '.join(map(str, solve(k, c))))


if __name__ == '__main__':
    main()