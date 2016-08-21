def solve(K, C, S):
    assert K == S
    if S < K - (C - 1):
        return "IMPOSSIBLE"
    return " ".join([str(i) for i in range(1, K + 1)])

T = int(input().strip())

for i in range(T):
    K, C, S = [int(i) for i in input().strip().split(" ")]
    print("Case #" + str(i+1) + ": " + solve(K, C, S))
