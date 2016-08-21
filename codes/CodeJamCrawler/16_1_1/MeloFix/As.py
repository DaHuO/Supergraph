T = int(input())

for loopC in range(1,T+1):

    S = input()

    RET = S[0]

    for x in S[1:]:
        if RET[0] <= x:
            RET = x+RET
        else:
            RET = RET+x

    print("Case #{}: {}".format(loopC,RET))
        
