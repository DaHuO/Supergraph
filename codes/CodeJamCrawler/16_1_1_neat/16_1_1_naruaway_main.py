def solve(S):
    s = S[0]
    for c in S[1:]:
        if c + s > s + c:
            s = c + s
        else:
            s = s + c
    return s



N = int(input())
for t in range(N):
    answer = solve(input())
    print('Case #{}: {}'.format(t + 1, answer))
