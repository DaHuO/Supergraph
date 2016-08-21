
import csv
import itertools
import copy
import time
import numpy as np


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L = csv_r.next()
        test_lst.append(L[0].upper())
    f.close() 
    return test_lst 


def process(w):
    if len(w) == 1:
        return [w]
    ll=process(w[1:])
    l=[]
    l.extend([w[0]+ww for ww in ll])
    l.extend([ww+w[0] for ww in ll])
    return l


def solve_test(test_case):
    l=process(''.join(reversed(test_case)))
    return max(l)
        

def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %s" % (1+i_test, res)


if __name__ == '__main__':
    #main('./A-large.in')
    #main('./simple.in')
    main('./A-small-attempt0.in')
    #main('./C-small-attempt0.in')

