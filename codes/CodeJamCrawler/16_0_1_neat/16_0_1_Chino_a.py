import sys

def find(N) :
    if N == 0 :
        return "INSOMNIA"
    s = set()
    l = N
    ret = 1
    while len(s) < 10 :
        l = ret*N
        tmp = str(l)
        for c in tmp :
            s.add(c)
            #print l, c, len(s)
        ret += 1
    return (ret-1)*N

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    #print(T)
    for i in range(T) :
        N = int(sys.stdin.readline())
        res = find(N)
        print "Case #%d: %s" % (i+1, str(res))
