import math


def solve(n, j):
    a = [0] * n
    a[0] = 1
    # smalles n digit eligible number's string representation
    s = "".join(str(x) for x in a)
    si2 = int(s, 2)

    count = 0

    # primes = set(sieve(int(s)))

    while count < j:
        # increment by 1
        si2 += 1
        s = str_base(si2, 2)
        # print(s)

        # check first and last digits to be 1
        if s[0] != "1" or s[-1] != "1":
            continue

        # check for non-primes in all bases
        non_prime_in_all_bases = True
        for base in range(2, 11):
            n = int(s, base)
            if is_prime(n):
                non_prime_in_all_bases = False
                break

        if non_prime_in_all_bases:
            count += 1
            print("{} {}".format(s, " ".join(str(x)
                                             for x in get_non_trivial_divisors(s))))


def get_non_trivial_divisors(s):
    # return non trivial divisors for each base in a list
    res = []
    for base in range(2, 11):
        n = int(s, base)
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                res.append(d)
                break
    return res


def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)


def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)


def is_prime(n):
    root = int(math.sqrt(n))
    for d in range(2, root + 1):
        if n % d == 0:
            return False
    return True


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))  # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):  # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i * i: np1: i] = [0] * len(range(i * i, np1, i))
    return filter(None, s)


if __name__ == "__main__":
    # f = open("coin_jam.in")

    t = int(input().strip())
    # t = int(f.readline().strip())
    for caseNo in range(1, t + 1):
        n, j = [int(v) for v in input().strip().split()]
        # n, j = [int(v) for v in f.readline().strip().split()]
        print("Case #{}:".format(caseNo))
        solve(n, j)

    # f.close()
