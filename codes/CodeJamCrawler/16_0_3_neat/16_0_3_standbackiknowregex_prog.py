def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def prime_or_first_factor(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
        return -1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return -1


n = 16
j = 50

counter = 2**(n-1) + 1
num_found = 0
o = open("fake.out", "w")
o.write("Case #1:\n")
while num_found < j and counter < 2**n:
    counter_base2 = baseN(counter, 2)
    jamcoin = format(int(counter_base2), "0" + str(n) + "d")
    factors = []
    for base in range(2,11):
        basenum = int(jamcoin, base)
        res = prime_or_first_factor(basenum)
        if res == -1:
            break
        else:
            factors.append(str(res))
    if len(factors) == 9:
        num_found += 1
        o.write("{} {}\n".format(jamcoin, " ".join(factors)))
    counter += 2

