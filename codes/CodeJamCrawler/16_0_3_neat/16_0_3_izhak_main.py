# -*- coding: utf-8 -*-
from math import sqrt


def find_divisor(i):
    if i <= 3:
        return i

    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            return j

    return i


def check_coin(s):
    divisors = []
    for i in range(2, 11):
        z = int(s, i)
        d = find_divisor(z)
        if d == z:
            return None
        divisors.append(d)
    return divisors


def mine_coins_NJ(N, J):
    j, i = 0, 1

    f = open("data/{}.txt".format(N), "w")

    while j < J:
        s = ("1{0:0" + str(N-2) + "b}1").format(i)
        divisors = check_coin(s)
        if divisors:
            j += 1
            line = "{} {}\n".format(s, " ".join([str(d) for d in divisors]))
            f.write(line)
            print line.strip()
        i += 1


def output_coins(N, J):
    f = open("data/{}.txt".format(N), "r")
    for i in range(0, J):
        line = f.readline().strip()
        print line



if __name__ == '__main__':
    # for i in range(2, 17):
    #     print mine_coins_NJ(i, 50)

    f = open("C-small-attempt0.in", "r")
    # f = open("example.txt", "r")
    t = int(f.readline())
    for i in xrange(1, t + 1):
        N, J = [int(s) for s in f.readline().split(" ")]
        print "Case #{}:".format(i)
        output_coins(N, 50)

