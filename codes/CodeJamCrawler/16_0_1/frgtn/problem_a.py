import sys


def solve(T, N):
    numbers = [False] * 10
    prev = None
    current = N
    i = 1
    while not all(numbers):
        current = N * i
        if current == prev:
            break
        prev = current
        for c in str(current):
            numbers[int(c)] = True
        i += 1

    if all(numbers):
        result = current
    else:
        result = 'INSOMNIA'
    print('Case #{}: {}'.format(T, result))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for case in range(n_cases):
        N = int(sys.stdin.readline().strip())
        solve(case + 1, N)


if __name__ == '__main__':
    main()
