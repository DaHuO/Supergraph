def spam(s, c):
    s1 = s + c
    s2 = c + s
    return s2 if s1 < s2 else s1

with open('A-large.in') as f:
    T = int(f.readline()[:-1])
    for i in range(T):
        S = f.readline()[:-1]
        ans = S[0]
        S = S[1:]
        for c in S:
            ans = spam(ans, c)
        print('Case #{0}: {1}'.format(i + 1, ans))
