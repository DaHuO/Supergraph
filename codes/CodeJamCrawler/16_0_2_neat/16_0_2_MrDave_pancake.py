
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
        test_lst.append(L[0])
    f.close() 
    return test_lst 


def flip(s):
    return ''.join(['+' if e == '-' else '-' for e in s])


def solve_test(test_case):
    q=collections.deque()
    q.append((0, test_case))
    already_seen=set()
    while True:
        n, c=q.popleft()
        if all([e=='+' for e in c]):
            return str(n)
        for i in xrange(1, len(c)+1):
            cc=flip(c[:i])+c[i:]
            if cc not in already_seen:
                q.append((n+1, cc))
            already_seen.add(cc) 


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %s" % (1+i_test, res)


if __name__ == '__main__':
    #main('./A-large.in')
    #main('./simple.in')
    main('./B-small-attempt1.in')
    #main('./C-small-attempt0.in')

