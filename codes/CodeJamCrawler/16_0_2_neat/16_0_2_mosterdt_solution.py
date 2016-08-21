#!/usr/bin/env python2

def case(T):
    pancakes = raw_input()
    return pancakes.count("+-") + pancakes.count("-+") + (pancakes[-1] == "-")

if __name__=="__main__":
    for i in xrange(int(raw_input())):
        print "Case #{}: {}".format(i+1, case(i))
