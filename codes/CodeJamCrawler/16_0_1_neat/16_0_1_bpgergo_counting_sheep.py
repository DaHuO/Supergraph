# https://code.google.com/codejam/contest/6254486/dashboard
import fileinput


def get_digits(n):
    result = set()
    while n:
        result.add(n % 10)
        n //= 10
    return result


def solve(n):
    if n == 0:
        return 'INSOMNIA'
    q = 1
    result = n
    digits = get_digits(result)
    while len(digits) < 10:
        q += 1
        result = q * n
        digits.update(get_digits(result))
    return result


if __name__ == '__main__':
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1,T+1):
        n = int(f.readline())
        print("Case #{0}: {1}".format(case, solve(n)))
