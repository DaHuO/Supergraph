def solve():
    B, M = map(int, input().split())
    if M > 2 ** (B-2):
        print("IMPOSSIBLE")
        return

    ans = [[ (1 if j>i else 0) for j in range(B)] for i in range(B)]
    ans[0] = [0] + [ 1 if (1 << j) & (M-1) else 0 for j in range(B-3, -1, -1)] + [1]

    print("POSSIBLE")
    print("\n".join("".join( map(str, row)) for row in ans))


T = int(input())
for t in range(T):
    print("Case #{}: ".format(t+1), end="")
    solve()
