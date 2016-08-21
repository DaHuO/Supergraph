T = int(input())
for t in range(1,T+1):
    k,c,s = map(int,input().split())
    print("Case #%d: "% t, end="")
    ret = list(range(1,s+1))
    print(*ret)
