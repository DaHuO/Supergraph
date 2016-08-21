T = int(raw_input())

for t in range(T):
    S = raw_input()
    res = S[0]
    for i in range(1, len(S)):
        if S[i] < res[0]:
            res = res + S[i]
        else:
            res = S[i] + res
    print 'Case #%d: %s' % (t+1, res)