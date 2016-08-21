alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert(len(alpha)==26)


def process(array):
    out = ""
    m=max(array)
    if m == 1:
       if sum(array)%2 == 1:
           i = array.index(m)
           array[i]-=1
           out+=alpha[i]
           return out


    i = array.index(m)
    c = array.count(m)
    if c==1:
        array[i]-=1
        out+=alpha[i]
    else:
        array[i]-=1
        out+=alpha[i]
        i = array.index(m)
        array[i]-=1
        out+=alpha[i]

    return out

def do(inp):
    solu = []
    while sum(inp)>0:
        m = float(max(inp))
        if 2*m > sum(inp):
             print "pb: ", inp
        o = process(inp)
        solu.append(o)
    return solu


import sys
T = int(sys.stdin.readline())
for t in range(T):
    sys.stdin.readline()
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    print "Case #%i:"%(t+1), ' '.join(do(array))




