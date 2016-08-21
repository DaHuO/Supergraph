from sys import stdin

T = int(stdin.readline().strip())

def solve(N):
    digits = set()
    digits_left = set(str(i) for i in range(10))
    for i in range(1, 362880 + 1):
        for digit in str(N * i):
            digits.add(digit)
        digits_left = digits_left.difference(digits)
        if len(digits_left) == 0:
            return N * i
    return 'INSOMNIA'

for case in range(1, T + 1):
    print('Case #{}: {}'.format(case, solve(int(stdin.readline().strip()))))
