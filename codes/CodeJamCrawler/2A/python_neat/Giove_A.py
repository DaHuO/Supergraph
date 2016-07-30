import sys
import random
import re
import itertools
import math
from collections import Counter
from multiprocessing import Pool

verbose = False


def read():
    # read data for a single test case
    n, r, p, s = [int(u) for u in sys.stdin.readline().split()]
    
    return n, r, p, s


def write(res):
    # write answer for a single test case
    print res


def order(string):
    if len(string) <= 1:
        return string
    
    n = len(string)
    assert n % 2 == 0
    
    m = n/2
    
    x = order(string[:m])
    y = order(string[m:])
    
    if x < y:
        return x+y
    else:
        return y+x
    
    


def solve(data):
    n, r, p, s = data
    
    res = n, r, p, s
    
    solutions = []
    
    for string in ['S', 'P', 'R']:
        for i in xrange(n):
            x = ''
            for c in string:
                if c == 'S':
                    x += 'PS'
                elif c == 'P':
                    x += 'PR'
                else:
                    x += 'RS'
            string = x
        
        if x.count('S') == s and x.count('P') == p and x.count('R') == r:
            # found a solution
            solutions.append(order(string))
        
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return min(solutions) if len(solutions) > 0 else "IMPOSSIBLE"


def check(data):
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return res


if __name__ == '__main__':
    check_mode = False
    parallelize = False
    
    if len(sys.argv) > 1 and "-v" in sys.argv[1:]:
        verbose = True
    
    if len(sys.argv) > 1 and "-c" in sys.argv[1:]:
        check_mode = True
    
    if len(sys.argv) > 1 and "-p" in sys.argv[1:]:
        parallelize = True
        i = sys.argv.index("-p")
        if len(sys.argv) > i+1 and sys.argv[i+1].isdigit():
            processes = int(sys.argv[i+1])
        else:
            processes = 2
        
    t = int(sys.stdin.readline())
    if verbose:
        print >> sys.stderr, "Solving %d test cases" % t
    
    # read input
    test_cases = [read() for i in xrange(t)]
    
    # solve
    if parallelize:
        process_pool = Pool(processes=processes)
        if check_mode:
            test_results = process_pool.map_async(check, test_cases).get(9999999)
        else:
            test_results = process_pool.map_async(solve, test_cases).get(9999999)
    
    else:
        if check_mode:
            test_results = [check(data) for data in test_cases]
        else:
            test_results = [solve(data) for data in test_cases]
    
    if verbose:
        sys.stderr.write("\n")
        sys.stderr.flush()
    
    # write output
    for i, res in enumerate(test_results):
        print "Case #%d:" % (i+1),
        write(res)


