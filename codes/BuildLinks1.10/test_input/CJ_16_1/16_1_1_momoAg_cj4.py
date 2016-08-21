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
    s = _input.readline().rsplit(' ')[0].rstrip()  # read a list of integers, 2 in this case
    print s 
    res = s[0]
    for c in range(1,len(s)):
        if (s[c]>=res[0]):
            print s[c]
            res=s[c]+res
        else:
            res=res+s[c]
    _output.write("Case #{}: {}\n".format(i,res))

_output.close()
_input.close()

