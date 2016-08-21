T = int(input())

for t in range(T):
    S = input().strip()

    s = S[0]
    for c in S[1:]:
        if c < s[0]:
            s = s + c
        else:
            s = c + s

    print("Case #" + str(t+1) + ": " + s)

