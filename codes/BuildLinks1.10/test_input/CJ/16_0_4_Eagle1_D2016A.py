T=int(input())
for t in range(0,T):
    K, C, S = [int(x) for x in input().split()]
    if K!=S:
        print("Case #%d: IMPOSSIBLE"%(t+1))
    else:
        print("Case #%d:"%(t+1),end="")
        for i in range(1,S+1):
            print(" %d"%i,end="")
        print("")
