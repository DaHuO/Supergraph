"""
Alexander Moriarty
Google Code Jam 2016
Problem A. Counting Sheep
"""
import sys

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
    
def count200(N):
    list_of_ints = list()
    n = None
    for n_ in xrange(1,200):
        list_of_ints += [int(i) for i in str(n_*N)]
        list_of_ints = f7(list_of_ints)
        if len(list_of_ints) == 10:
            n = n_
            break

    if len(list_of_ints) != 10:
        return "INSOMNIA"
    else:
        return str(n*N)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _t in xrange(T):        
        N = int(f.readline())
        n = count200(N)
        print "Case #%d: %s" % (_t+1, n)
