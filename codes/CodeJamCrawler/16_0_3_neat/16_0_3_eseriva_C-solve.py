#!/usr/bin/pypy

import sys
infile = sys.argv[1]
try:
    outfile = sys.argv[2]
except IndexError:
    outfile = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in xrange(no_lines):
        retval.append(f.readline().rstrip())
    return retval

numbers = "0123456789"

def numtostr(num, base):
    retval = []
    while num>0:
        num, mod = divmod(num, base)
        retval.append(numbers[mod])
    
    return "".join(reversed(retval))

LARGENUM = 10**6
def solve(n, j):
    retval = []
    
    start = 2**(n-1)+1
    end = 2**n-1
    
    i = start
    while i<=end:
        print "len", len(retval)
        
        if len(retval) == j:
            break
            
        divisors = []
        for base in xrange(2, 11):
            num = int("{:b}".format(i), base)
            for d in xrange(2, min(num/2, LARGENUM+1)):
                if num % d == 0 and d not in divisors:
                    divisors.append(d)
                    break
            else:
                break
        
        if len(divisors) == 9:
            retval.append("{:b} {}".format(i, " ".join(map(str, divisors))))
            print i, divisors
        
        i = i + 2
        
    return retval
    
def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    out = open(outfile, "w")
    
    for case_idx in xrange(no_cases):
        n, j = read_ints(f)
        sols = solve(n, j)
        out.write("Case #%d:\n" % (case_idx+1))
        out.write("%s" % "\n".join(sols))
        

if __name__ == "__main__":
    main()
    
    