import math


def solve():
    f = open("C-large.in", "r")
    T = int(f.readline())
    out = open("output.txt", "w")

    primes = [3, 5, 7]
    x = 11
    while x < 67000:
        isprime = True
        for p in primes:
            if x % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(x)
        x += 2

    for case in range(T):
        N, J = map(int, f.readline().strip().split())

        coinjam = (1 << (N - 1)) + 1
        num = 0
        divs = []
        coins = []

        while num < J:

            base = 2
            divisors = [0 for i in range(9)]
            while base <= 10:
                value = int("{0:b}".format(coinjam), base)
                for p in primes:
                    if value % p == 0:
                        if value == p:
                            break
                        divisors[base - 2] = p
                        break
                if divisors[base - 2] == 0:
                    break
                else:
                    base += 1
            if 0 not in divisors:
                coins.append(coinjam)
                divs.append(divisors)
                num += 1
            coinjam += 2

        print("Case #%d:" % (case + 1))
        out.write("Case #%d:\n" % (case + 1))
        for i in range(len(coins)):
            out.write("{0:b} ".format(coins[i]))
            print("{0:b} ".format(coins[i]), end='')
            for div in divs[i]:
                out.write("%d " % (div))
                print("%d " % (div), end='')
            out.write("\n")
            print()


solve()
