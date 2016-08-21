# -*- coding: utf-8 -*-


def solve(x):

    if x == 0:
        return "INSOMNIA"

    q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while any([qx == 0 for qx in q]):
        i += 1
        z = list(str(x * i))
        for n in z:
            q[int(n)] += 1

    return x * i


if __name__ == '__main__':
    # f = open("example.txt", "r")
    # f = open("A-small-attempt0.in", "r")
    f = open("A-large.in", "r")
    t = int(f.readline())
    for i in xrange(1, t + 1):
        x = int(f.readline())
        r = solve(x)
        print "Case #{}: {}".format(i, r)

