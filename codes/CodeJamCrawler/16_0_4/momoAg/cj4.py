import sys
import pyprimes

path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output


_input = open(path_input,"r")
_output = open(path_output,"w")


t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    K, C, S = [int(s) for s in _input.readline().split(" ")]  # read a list of integers, 2 in this case
    print K, C, S
    if (K!=S):
        _output.write("Case #{}: {}\n".format(i,"IMPOSSIBLE"))
    else:
        res = [1+K**(C-1)*j for j in range(K)]
        _output.write("Case #{}: {}\n".format(i,' '.join([str(j) for j in res])))

_output.close()
_input.close()

