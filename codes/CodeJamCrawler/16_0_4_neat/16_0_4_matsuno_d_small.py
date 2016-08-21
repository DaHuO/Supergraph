import sys

def do(K, C, S):
    if C == 1:
        for i in xrange(1, S + 1):
            print i,
        print 
        return

    if K == 1:
        print 1
        return 

    for i in xrange(2, S + 1):
        print i,
    print 

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        K, C, S = [int(e) for e in sys.stdin.readline().split()]
        print "Case #{0}:".format(i + 1),
        do(K, C, S)

if __name__ == '__main__':
    main()
