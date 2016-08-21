T=int(input())
for t in range(0,T):
    S=input()
    if len(S)>0:
        if S[len(S)-1]=='-':
            c=1
        else:
            c=0
        for i in range(len(S)-2,-1,-1):
            if S[i]!=S[i+1]:
                c+=1
    else:
        c=0
    print("Case #%d: %d"%(t+1,c))
