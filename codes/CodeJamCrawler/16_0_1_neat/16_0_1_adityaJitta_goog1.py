import pdb
import sys
import getopt
from collections import defaultdict
from sets import Set

def explore_sheep(N):
    #import pdb;pdb.set_trace()
    sN = str(N)
    sn_array = Set([sN[i] for i in range(len(sN))])
    val = len(sn_array)
    k = 1
    while (val < 10):
        k += 1
        new_N = k*N
        sn = str(new_N)
        sn_array_new = Set([sn[i] for i in range(len(sn))])
        union_set = Set.union(sn_array_new, sn_array)
        val = len(union_set)
        sn_array = union_set
    return new_N

explore_sheep(2)

def getRes(temp):
    outname = "/Users/Work/Desktop/output.txt"
    fh1 = open(outname, 'w')
    for i in range(len(temp)):
        N = temp[i]
        count = i + 1
        print N
        if (N == 0):
            print N
            newstr = "INSOMNIA"
            tstr = "Case #"+str(count)+": "+newstr
            print >>fh1, tstr
        else:
            res = explore_sheep(N)
            tstr = "Case #"+str(count)+": "+str(res)
            print >>fh1, tstr
    fh1.close()
    



def main():
    fname = sys.argv[1]
    fh = open(fname, 'r')
    count = 0
    temp = []
    tot_num = 0
    for l in fh:
        if(count == 0):
            tot_num = int(l.strip())
        if(count > 0):
            temp.append(int(l.strip()))
        count += 1
    getRes(temp)
    fh.close()

if __name__ == '__main__':
    main()