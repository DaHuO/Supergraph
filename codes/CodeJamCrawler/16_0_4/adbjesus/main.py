def solve():
    K,C,S = [int(i) for i in input().split()]
    for i in range(1,K):
        print("%d " % (i),end="")
    print(K)

T = int(input())
for t in range(1,T+1):
    print("Case #%d: " % (t), end="")
    solve()
