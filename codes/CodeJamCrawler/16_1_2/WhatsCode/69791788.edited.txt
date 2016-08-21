T = int(raw_input())
for i in xrange(T):
    ans = []
    dic = {}
    N = int(raw_input())
    for j in xrange(2*N-1):
        a = raw_input().split()
        for aa in a:
            if aa in dic:
                dic[aa] += 1
            else:
                dic[aa] = 1
    for d in dic:
        if dic[d] % 2 == 1:
            ans.append(d)
    ans = map(int, ans)
    ans.sort()
    ans = map(str, ans)
    print "Case #"+str(i+1)+": "+' '.join(ans)
