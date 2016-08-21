from __future__ import print_function, division
import sys
from collections import defaultdict
from random import randint

def read_case(f):
    return (int(f.readline()))

def print_case(result, n, f):
    text = "Case #%d: %s" % (n,result)
    out.write(text + '\n')
    print(text)
    
def do_case(case):
    n = case
    
    if n == 0:
        return 'INSOMNIA'
    seen = set()
    for i in range(1, 10**6):
        t = i*n
        seen |= set(str(t))
        
        if len(seen) == 10:
            print(n, i)
            return t

in_ = open(sys.argv[1], 'r')
num_cases = int(in_.readline())
cases = [read_case(in_) for n in range(num_cases)]
#cases = [randint(0,10**6+1) for i in range(1000)]
    
results = [do_case(case) for case in cases]

out = open(sys.argv[2], 'w')
for n,result in enumerate(results):
    print_case(result, n+1, out)

