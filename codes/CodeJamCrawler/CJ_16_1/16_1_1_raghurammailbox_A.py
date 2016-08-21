T=int(raw_input())

for t in range(0,T):
    S=raw_input()
    first=S[0]
    winner=S[0]
    for s in S[1:]:
        if ord(s)>=ord(first):
            winner=s+winner
            first=s
        else:
            winner=winner+s
    print "Case #"+str(t+1)+": "+winner
