
import csv
import itertools
import copy
import time


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L = csv_r.next()
        test_lst.append([int(L[0]),])
    f.close() 
    return test_lst 



def solve_test(test_case):
    l, already_seen=set(), set()
    i=1
    while True: 
        n=test_case*i
        l.update([e for e in str(n)])
        if len(l)==10:
            return i*test_case
        if n in already_seen:
            return "INSOMNIA"
        already_seen.add(n)
        i=i+1


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case[0])
        print "Case #%i: %s" % (1+i_test, res)


if __name__ == '__main__':
    main('./A-large.in')
    #main('./simple.in')
    #main('./A-small-attempt0.in')
    #main('./C-small-attempt0.in')

