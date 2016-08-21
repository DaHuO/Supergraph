def sol(S):
    dp = [[0] * 101, [0] * 101]
    for i in range(len(S)):
        if S[i] == '+':
            dp[0][i+1] = min(dp[0][i], dp[1][i] + 1)
            dp[1][i+1] = min(dp[0][i] + 1, dp[1][i] + 2)
        else:
            dp[0][i+1] = min(dp[0][i] + 2, dp[1][i] + 1)
            dp[1][i+1] = min(dp[0][i] + 1, dp[1][i])

    return min(dp[0][len(S)], dp[1][len(S)]+1)

T = int(raw_input())
for i in range(T):
    S = raw_input()
    print("Case #{0}: {1}".format(i+1, sol(S)))
