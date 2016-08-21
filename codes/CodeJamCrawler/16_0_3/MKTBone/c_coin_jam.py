import fileinput
import itertools


def non_trivial_divisor(n):
    if n > 2 and n % 2 == 0:
        return 2
    d = 3
    # shortcut: skip large divisors, there are other jamcoins to be had
    while d * d <= n and d < 50:
        if n % d == 0:
            return d
        d += 2
    return None


def as_base(jam_cand, base):
    mult, val = 1, 0
    for digit in reversed(jam_cand):
        val += digit * mult
        mult *= base
    return val


def all_bases(jam_cand):
    return (as_base(jam_cand, base) for base in range(2, 11))


def jam_cands(n):
    return ((1,) + mid + (1,) for mid in itertools.product([0, 1], repeat=(n - 2)))


cases = [[int(x) for x in line.split()] for line in list(fileinput.input())[1:]]
for i, (n, j) in enumerate(cases):
    print("Case #{}:".format(i + 1))
    for jam_cand in jam_cands(n):
        if j == 0:
            break
        divisors = []
        for jam_base in all_bases(jam_cand):
            d = non_trivial_divisor(jam_base)
            if d is None:
                break
            divisors.append(d)
        if len(divisors) == 9:
            j -= 1
            print(as_base(jam_cand, 10), " ".join([str(x) for x in divisors]))
    assert j == 0
