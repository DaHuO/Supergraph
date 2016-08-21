T = int(input())
for t in range(1,T+1):
    print("Case #%d: " % t, end="")
    s = input()
    minus = (s[0] == '-')
    p = int(minus)
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            p += int(s[i] == '-')
    print(2*p-minus)

