#!/usr/bin/env python

def get_digits(n):
    if n == 0:
        return set([0])
    x = []
    while n != 0:
        x.append(n % 10)
        n = n / 10
    return set(x)

def last_number(n):
    # print n
    if n == 0:
        return "INSOMNIA"
    digits_left = set(range(10))
    x = 1
    while True:
        digits_n = get_digits(x * n)
        digits_left = digits_left.difference(digits_n)
        # print n, x, digits_n, digits_left
        if digits_left == set():
            return n * x
        x += 1

def main():
    with open("in") as f:
        t = int(f.readline())
        for i in xrange(1, t + 1):
            n = int(f.readline())
            print "Case #{0}: {1}".format(i, last_number(n))



if __name__ == '__main__':
    main()