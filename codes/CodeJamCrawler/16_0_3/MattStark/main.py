import sys


print("Case #1:")


def factor(n):
    for i in range(2, min(int(n ** 0.5) + 1, 1000)):
        if n % i == 0: return i
    return None


def solve(n, j):
    n = int(n)
    j = int(j)
    results = []
    for i in range(1 << (n - 2)):
        num = "1" + bin(i)[2:].zfill(n - 2) + "1"
        factors = []
        for base in range(2, 11):
            factors.append(factor(int(num, base)))
            if factors[-1] is None: break

        if None not in factors:
            results.append((num, factors))
            print(" ".join(map(str, [num] + factors)))
            if len(results) == j: return


if __name__ == '__main__':
    solve(32, 500)
