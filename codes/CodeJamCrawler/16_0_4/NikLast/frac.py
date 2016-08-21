n = int(raw_input())
for case in range(n):
    k,c,s = (int(res) for res in raw_input().split())

    check = []
    cursor = 0
    if k==1:
        check.append('1')
    elif c==1:
        for k2 in range(k):
           check.append("%d" % (k2+1))
    else:
        for cursor in range(k-1):
            check_cand = (k*cursor)+cursor+2
            check.append("%d" % check_cand)
            
    if len(check)>s:
        output = "IMPOSSIBLE"
    else:
        output = " ".join(check)

    print "Case #%d: %s" % (case+1, output)
