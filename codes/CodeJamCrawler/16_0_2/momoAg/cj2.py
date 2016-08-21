
import sys
import re

path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output


_input = open(path_input,"r")
_output = open(path_output,"w")


t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in _input.readline().split(" ")]  # read a list of integers, 2 in this case
    stack = _input.readline().rsplit()[0]
    flatten = re.sub(r'(\+)\1+', r'\1', stack)
    flatten = re.sub(r'(\-)\1+', r'\1', flatten)
    if(flatten[-1]=='+'):
        flatten=flatten[:-1]
    res=len(flatten)
    _output.write("Case #{}: {}\n".format(i, res))
_output.close()
_input.close()
 
