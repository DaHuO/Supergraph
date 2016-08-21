T = int(raw_input())

for kase in range(1,T+1):
    S = raw_input()
    ans = S[0]
    for i in range(1,len(S)):
        if S[i] < ans[0]:
            ans += S[i]
        else:
            ans = S[i]+ans
    print "Case #"+str(kase)+": "+ans
