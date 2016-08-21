#! /usr/bin/python

from sys import stdin

def find_last_number(starting_num):
    tracker = set()
    N = starting_num
    if N == 0:
        return "INSOMNIA"

    count = 1
    while tracker != set([0,1,2,3,4,5,6,7,8,9]):
        N = starting_num * count
        dig = N
        while dig:
            if (dig % 10) not in tracker:
                tracker.add(dig % 10)
            dig //= 10
        count += 1
    return N

T = int(stdin.readline())

for t in xrange(T):
    N = int(stdin.readline())
    print "Case #%d: %s" % (t+1, find_last_number(N))