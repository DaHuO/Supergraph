import sys

for cases in xrange(int(sys.stdin.readline())):
    K,C,S = map(int,sys.stdin.readline().split())
    if K == 1:
        l = [1]
    elif C == 1:
        l = [i for i in xrange(1,K+1)]
    else:
        l = []
        mid = (K**C)/2
        S -= 1
        l.append(mid)
        left = mid-1
        right = mid+1
        while S > 0:
            l.append(left)
            S -= 1
            if (S>0):
                l.append(right)
                S -= 1
            left -= 1
            right += 1
    ans = ''
    l.sort()
    for i in l: ans += '%d '%(i)
    print "Case #%d: %s"%(cases+1,ans)
