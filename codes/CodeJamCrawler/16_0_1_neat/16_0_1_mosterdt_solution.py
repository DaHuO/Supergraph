#!/usr/bin/env python2

def case(T):
    step = int(raw_input())
    numbers_seen = set()
    number = 0
    if step == 0:
        return "INSOMNIA"
    while len(numbers_seen) < 10:
        number += step
        [numbers_seen.add(i) for i in list(str(number))]
        #print numbers_seen
    return number




if __name__=="__main__":
    for i in xrange(int(raw_input())):
        print "Case #{}: {}".format(i+1, case(i))
