# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys
from sets import Set

path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output

_input = open(path_input,"r")
_output = open(path_output,"w")

to_see = Set(range(0,10))

t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in _input.readline().split(" ")]  # read a list of integers, 2 in this case
    n = int(_input.readline())
    if (n==0): 
        res = "INSOMNIA"
    else:
        _length=0
        j=0
        seen_numbers=Set([])
        while(_length<10):
            j+=1
            new_seen_numbers=Set([int(k) for k in list(str(j*n))])
            seen_numbers=seen_numbers.union(new_seen_numbers)
            _length = len(to_see&seen_numbers)
        res=j*n
    _output.write("Case #{}: {}\n".format(i, res))
_output.close()
_input.close()
    # check out .format's specification for more formatting options
