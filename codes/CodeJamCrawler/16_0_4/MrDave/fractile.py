
import csv
import itertools
import copy
import time
import collections


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L = csv_r.next()
        test_lst.append([int(e) for e in L])
    f.close() 
    return test_lst 


def solve_test(test_case):
    k, c, s=test_case
    n=k**(c-1)
    l=[str(i*n) for i in xrange(1,min(k,s)+1)]
    return l


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        if type(res) == str:
            pass
        else:
            print "Case #%i: %s" % (1+i_test, ' '.join(res))


if __name__ == '__main__':
    #main('./simple.in')
    main('./D-small-attempt0.in')

