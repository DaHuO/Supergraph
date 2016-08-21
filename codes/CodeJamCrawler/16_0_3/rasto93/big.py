import string
import sys


def to_base(x, b):
    res = ""
    while x > 0:
        res += string.digits[x % b]
        x //= b

    return res[::-1]


def from_base(s, b):
    res = 0
    for c in s:
        res = res * b + (ord(c) - ord('0'))

    return res

needs_to_find = 500
for i in range(2**29,2**30):
    jamcoin = "1%s1" % to_base(i, 2)
    ok = True
    divs = []
    for b in range(2, 11):
        jamcoin_b = from_base(jamcoin, b)
        ok = False
        for num in range(2, min(10**4, jamcoin_b - 1)):
            if jamcoin_b % num == 0:
                divs.append(num)
                ok = True
                break

        if not ok:
            break

    if ok:
        print(jamcoin + " " + ' '.join(map(str, divs)))
        needs_to_find -= 1
        if needs_to_find == 0:
            sys.exit(0)
