rest = []
ans = []
def dfs(now, depth, pos):
    if depth == n:
        cur = pos-2**n
        #print pos, cur, now
        ans[cur] = "RPS"[now]
        rest[now] -= 1
        return 1
    if rest[now]==0 or rest[now-1]==0:
        return 0
    if dfs(now, depth+1, 2*pos)==0 or dfs((now+2)%3, depth+1, 2*pos+1)==0:
        return 0
    le = (2*pos)*2**(n-depth-1)-2**n
    ri = (2*pos+1)*2**(n-depth-1)-2**n
    smaller = 0
    for i in xrange(ri-le):
        if ans[ri+i] < ans[le+i]:
            smaller = 1
            break
    if smaller:
        for i in xrange(ri-le):
            ans[ri+i],ans[le+i] = ans[le+i],ans[ri+i]
    #print "pd", pos, depth
    #print depth, pos, le, ri
    return 1

for t in xrange(input()):
    print "Case #%d:"%(t+1),

    n, r, p, s = map(int, raw_input().split())
    ans = [4]*2**n
    res = "~"

    for i in xrange(3):
        rest = [r, p, s]
        if dfs(i, 0, 1):
            res = min(res, "".join(ans))
            break
    else:
        print "IMPOSSIBLE"
        continue
    print res

