T = int(raw_input())

def recursive_sort(s):
    if len(s) == 2:
        return "".join(sorted(s))
    else:
        return "".join(sorted([recursive_sort(s[:len(s)/2]), recursive_sort(s[len(s)/2:])]))


dj = {"S": "PS", "R": "RS", "P": "PR"}
for t in xrange(T):
    N, R, P, S = [int(x) for x in raw_input().split()]
    ssr = "R"
    ssp = "P"
    sss = "S"
    for n in xrange(N):
        nssr = ""
        for i in ssr:
            nssr += dj[i]
        ssr = nssr
        nssp = ""
        for i in ssp:
            nssp += dj[i]
        ssp = nssp
        nsss = ""
        for i in sss:
            nsss += dj[i]
        sss = nsss
    sort_ssr = "".join(sorted(ssr))
    sort_ssp = "".join(sorted(ssp))
    sort_sss = "".join(sorted(sss))
    target = P*"P" + R*"R" + S*"S"
    if sort_ssp == target:
        print "Case #" + str(t+1) + ": " + recursive_sort(ssp)
    elif sort_sss == target:
        print "Case #" + str(t+1) + ": " + recursive_sort(sss)
    elif sort_ssr == target:
        print "Case #" + str(t+1) + ": " + recursive_sort(ssr)
    else:
        print "Case #" + str(t+1) + ": IMPOSSIBLE"
