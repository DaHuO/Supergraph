t = int(input())
for _ in range(t):
    s = input()
    s += "+"
    cnt= 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cnt += 1
    print("Case #%d: %d" % (_+1, cnt))
