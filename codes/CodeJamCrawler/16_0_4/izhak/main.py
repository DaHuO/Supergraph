# -*- coding: utf-8 -*-


def solve(K, C, S):
    if S < K:
        return None
    l = K ** (C - 1)
    return " ".join([str(l * i) for i in range(1, S + 1)])


if __name__ == '__main__':
    # f = open("example.txt", "r")
    f = open("D-small-attempt2.in", "r")
    # f = open("D-large.in", "r")
    t = int(f.readline())
    for i in xrange(1, t + 1):
        K, C, S = [int(s) for s in f.readline().split(" ")]
        r = solve(K, C, S)
        if r:
            print "Case #{}: {}".format(i, r)
        else:
            print "Case #: IMPOSSIBLE"
