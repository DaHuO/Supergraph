T = int(input())
for test in range(1, T + 1):
    S = '+' + input()[::-1]
    answer = 0
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            answer += 1
    print("Case #%d: %d" % (test, answer))
