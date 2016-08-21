import sys


def flip(pancakes, k):
    return (tuple(reversed(tuple(map(lambda p: not p, pancakes[:k + 1])))) +
            pancakes[k + 1:])


def get_last_blank(pancakes):
    for k, p in enumerate(pancakes):
        if not p:
            last_blank = k
    return last_blank


def iterative_solve(pancakes):
    steps = 0
    while not all(pancakes):
        last_blank = get_last_blank(pancakes)
        if not pancakes[0]:
            pancakes = flip(pancakes, last_blank)
        else:
            pancakes = flip(pancakes, pancakes.index(False) - 1)

        steps += 1
    return steps


def solve(T, line):
    global _seen_states
    pancakes = tuple(c == '+' for c in line.strip())
    _seen_states = set()
    steps = iterative_solve(pancakes)
    print('Case #{}: {}'.format(T, steps))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for case in range(n_cases):
        line = sys.stdin.readline()
        solve(case + 1, line)


if __name__ == '__main__':
    main()
