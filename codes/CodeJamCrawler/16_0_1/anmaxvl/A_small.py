import sys
import time

def solve(n):
    if n==0:
        return None

    digs = set()
    i = 1
    while len(digs) < 10:
        t = i*n
        while t>0:
            digs.add(t%10)
            t/=10
        i += 1

    return (i-1)*n


if __name__=='__main__':
    # from gen_A import gen
    # gen()
    # time.sleep(.5)
    # tstart = time.time()
    t = int(sys.stdin.readline().strip())

    for i in range(t):
        n = int(sys.stdin.readline().strip())
        res = solve(n)
        if res is None:
            print 'Case #%d: INSOMNIA' % (i+1)
        else:
            print 'Case #%d: %d' % (i+1, res)

    # tfinish = time.time()
    #
    # print
    # print 'Time elapsed: %1.10f' % (tfinish-tstart)
