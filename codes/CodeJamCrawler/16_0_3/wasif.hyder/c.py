import random
import pyprimes
from fractions import gcd

def brent(N):
    if N % 2 == 0:
        return 2
    if N % 10 == 0:
        return 10
    y, c, m = random.randint(1, N - 1), random.randint(1, N - 1), random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while (k < r and g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r = r * 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break

    return g



def base10toN(num, base):
    # From http://code.activestate.com/recipes/577586-converts-from-decimal-to-any-base-between-2-and-26/
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

def isPrime2(n):
    # http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True

def solution(N, J):
    result = ""
    string = "1{:0%sb}1" % str(N-2)

    possible_jamcoins = method_name3(N, string)
    if N == 2:
        possible_jamcoins = ['11']
    valid_jamcoins = []
    for possible_jamcoin in possible_jamcoins:
        # Generates all bases of a number
        canidates = method_name(possible_jamcoin)
        canidates_true = method_name2(possible_jamcoin)
        if True not in canidates_true:
            # print(canidates)
            valid_jamcoins.append((possible_jamcoin, canidates))
        if len(valid_jamcoins) >= J:
            break
    for i, jamcoin in enumerate(random.sample(valid_jamcoins, J)):
        result += "{} {}\n".format(jamcoin[0], " ".join(([str(brent(x)) for x in jamcoin[1]])))
        #print([base10toN(possible_jamcoin, i) for i in range(2,11)])
    # return [int(x, base=2) for x in possible_jamcoins]
    # return [x for x in possible_jamcoins]
    return result[:-1]


def method_name3(N, string):
    for i in range(0, 2**(N-2)):
        yield string.format(i)


def method_name2(possible_jamcoin):
    return [pyprimes.isprime((int(possible_jamcoin, base=i))) for i in range(2, 11)]


def method_name(possible_jamcoin):
    return [int(possible_jamcoin, base=i) for i in range(2, 11)]


if __name__ == "__main__":
    with open("c.in", "r") as inp, open("cout.in", "w") as out:
        x = [(line.strip()) for line in inp.readlines()]
        cases = int(x[0])
        x = x[1:]
        for case, line in enumerate(x):
            N, J = tuple([int(x) for x in line.split()])
            N, J = 32, 500
            print("Case #{}:\n{}\n".format(case+1, (solution(N, J))))
            out.write("Case #{}:\n{}\n".format(case+1, solution(N, J)))
