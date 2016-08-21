#/bin/usr/env python
import math
import sys


def generator(size):
    i = 1
    while(i < size):
        i += 2
        yield i


def main():
    T = int(raw_input())
    print "Case #1:"
    N, J = map(int, raw_input().split())
    primes = [2]
    g = generator(655360)
    for i in g:
        flag = True
        ri = int(math.sqrt(i) + 1)
        for j in primes:
            if j > ri:
                break
            if i % j == 0:
               flag = False
               break
        if flag:
            primes.append(i)

    j = 0
    for i in range((1 << (N - 1)) + 1, (1 << N), 2):
        if j == J:
            break
        bstr = bin(i)[2:]
        divs = []
        for base in range(2, 11, 1):
            x = int(bstr, base)
            rx = int(math.sqrt(x)) + 1
            f = False
            for p in primes:
                if p > rx:
                    break
                if x % p == 0:
                    divs.append(p)
                    f = True
                    break
            if f==False:
                break
        if divs.__len__() == 9:
            print "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(bstr, divs[0], divs[1], divs[2], divs[3], divs[4], divs[5], divs[6], divs[7], divs[8])
            j = j+1


if __name__ == "__main__":
    main()
