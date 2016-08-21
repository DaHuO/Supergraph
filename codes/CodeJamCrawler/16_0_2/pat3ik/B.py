t = int(raw_input())

for tt in range(1,t + 1):
    s = raw_input()
    ans = 0
    plus = s[0] == '+'
    for i in range(1,len(s)):
        if (s[i] == '+') != plus:
            ans += 1
            plus = not plus
    if not plus:
        ans += 1
    print "Case %s%d: %d" % ('#',tt,ans)     