import sys
import pyprimes
import pyprimes.factors
from math import *
import string
path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output


_input = open(path_input,"r")
_output = open(path_output,"w")


t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    res = ""
    N = int(_input.readline().split(" ")[0])
    parties = [int(s) for s in _input.readline().split(" ")]  # read a list of integers, 2 in this case
    parties_names = string.ascii_uppercase[0:len(parties)]
    parties_zipepd = zip(parties,parties_names)
    parties_zipepd = sorted(parties_zipepd,reverse=True)
    print "zipped",parties_zipepd
    if(sum(parties)%2==1):
        res+=parties_zipepd[0][1]+" "
        parties_zipepd[0]=(parties_zipepd[0][0]-1,parties_zipepd[0][1])
        parties_zipepd = [k for k in parties_zipepd if k[0]>0]
    while (len(parties_zipepd)>0):
        res += parties_zipepd[0][1] + parties_zipepd[1][1]+" "
        parties_zipepd[0] = (parties_zipepd[0][0]-1,parties_zipepd[0][1])
        parties_zipepd[1] = (parties_zipepd[1][0]-1,parties_zipepd[1][1])
        parties_zipepd = [k for k in parties_zipepd if k[0]>0]
        parties_zipepd = sorted(parties_zipepd,reverse=True)
        print parties_zipepd
        print i

    print res
    _output.write("Case #{}: {}\n".format(i,res))
_output.close()
_input.close()

