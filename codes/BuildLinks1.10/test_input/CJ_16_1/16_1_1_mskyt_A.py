import sys

def solve(S):
    ret = ""
    for k in S:
        if k+ret > ret+k:
            ret = k+ret
        else:
            ret = ret+k
    return ret

    

if __name__ == "__main__":
    fd = open( sys.argv[1] )
    T = int( fd.readline() )
    for t in xrange(T):
        n = fd.readline().strip()
        s = solve(n)
        print "Case #%d: %s" % (t+1,s)
    fd.close()
