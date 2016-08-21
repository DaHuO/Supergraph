t = int(raw_input())
for i in xrange(1, t + 1):
    ans = []
    n, m, p = [int(s) for s in raw_input().split(" ")]
    if m == 1 and n > t:
        ans = "IMPOSSIBLE"
    elif m == 1:
        for j in range(1,n+1):
            ans.append(j)
    else:
        ans = []
        briks = -1
        for briks in range(1,n,2):
            ans.append(n * (briks - 1) + (briks + 1))
        if n%2 != 0:
            ans.append(n*(briks+1)+(briks+2))
    if len(ans) > p:
        print "Case #"+str(i)+':'+ " IMPOSSIBLE"
    else:
        print "Case #"+str(i)+':'+ ' ' + ' '.join(map(str, ans))
    #print ans
    #print "Case #{}: {} {}".format(i, n + m, n * m)
