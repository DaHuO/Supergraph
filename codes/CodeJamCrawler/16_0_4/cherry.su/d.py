def solve(K, C, S):
    if K == 1:
        return "1"

    l = []
    for i in range(1, K+1):
        ix = (i-1)*((K**C - K)//(K - 1)) + i
        l.append(str(ix))
    return ' '.join(l)

if '__main__' == __name__:
    T = int(raw_input())
    for _t in range(T):
        K, C, S = map(int, raw_input().strip().split())
        print "Case #%d: %s" % (_t + 1, solve(K, C, S))
