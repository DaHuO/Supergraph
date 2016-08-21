#!/usr/bin/python

"""Counting sheep from google code jam qualification round of 2016."""

def num_sleep(n):
    """Returns the number sheep falls asleep."""
    if n == 0:
        return "INSOMNIA"
    seen = set()
    curr_n = n
    while True:
        #print seen, curr_n
        for d in str(curr_n):
            seen.add(d)
        if len(seen) == 10:
            return curr_n
        curr_n += n

#Testing code
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    n = int(raw_input())

    print "Case #{}: {}".format(i, num_sleep(n))
  # check out .format's specification for more formatting options
