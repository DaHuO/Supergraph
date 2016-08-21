
def solve(t):
    K, C, S = map(int, raw_input().split())
    print "Case #%d:"%(t+1),
    
    if C*S < K:
        print "IMPOSSIBLE"
    else:
        inds = range(K)+[0]*C
        for i in xrange( ((K-1)/C)+1):
            have = 0
            for x in inds[i*C:(i+1)*C]:
                have = K*have + x
            print have+1,
        print

def main():
    T = input()
    for i in xrange(T):
        solve(i)
    
if __name__=="__main__":
    main()