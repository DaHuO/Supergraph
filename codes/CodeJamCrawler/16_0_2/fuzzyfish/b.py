
T = int(input())

for ttt in range(T):
    ans = 0
    iscounting = False
    temp = True
    s = input()
    for ind in range(len(s)-1, -1, -1):
        if iscounting:
            if not (s[ind] == s[ind+1]):
                ans += 1
        else:
            if s[ind] == '-':
                iscounting = True
                ans += 1

    print("Case #%d: %d" % (ttt+1, ans))
