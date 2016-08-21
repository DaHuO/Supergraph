import fileinput
import collections
import numpy as np

def compute(M):
    d =collections.defaultdict(int)
    for row in M:
        for a in row:
            d[int(a)] +=1
    lst = [k for k in d.keys() if d[k]%2 !=0]
    lst.sort()
    return lst




if __name__ == "__main__":

    f = fileinput.input()
    T=int(f.readline())
    for case in xrange(1,T+1):
        N = int(f.readline())
        M = np.zeros((2*N-1, N),dtype=int)
        for i in xrange(2*N-1):
            M[i,:] = np.array([int(j) for j in f.readline().strip().split()])
        print("Case #{0}: {1}".format(case, ' '.join([str(i) for i in compute(M)])))

