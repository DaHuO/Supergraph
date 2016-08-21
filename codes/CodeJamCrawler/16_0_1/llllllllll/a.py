import sys

from toolz import drop


max_cases = 1e6


def cases(f):
    return map(int, drop(1, f))


def run_case(n):
    expected = set(map(str, range(10)))
    seen = set()
    count = 0
    while seen != expected and count < max_cases:
        count += 1
        seen |= set(str(n * count))
    if count == max_cases:
        return 'INSOMNIA'
    return count * n


def main():
    for n, result in enumerate(map(run_case, cases(sys.stdin)), 1):
        print('Case #%d: %s' % (n, result))


if __name__ == '__main__':
    main()
