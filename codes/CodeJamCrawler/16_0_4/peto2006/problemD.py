n = int(input())
for case in range(1, n+1):
    k, c, s = (int(x) for x in input().split())
    print("Case #", case, ": ", " ".join([str(x) for x in range(1, s+1)]), sep="")
