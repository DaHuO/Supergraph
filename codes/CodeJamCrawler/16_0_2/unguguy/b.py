def flip(x, y, s):
    sub = s[x:y + 1][::-1]
    sub = ''.join(['+' if ch == '-' else '-' for ch in sub])
    return s[:x] + sub + s[y+1:]

n = int(input())
for tc in range(1, n + 1):
    s = input()
    ans = 0
    while True:
        pos_neg = s.find('-')
        if pos_neg == -1:
            break
        pos_plus = s.find('+')
        if s[0] == '-':
            if pos_plus == -1:
                ans += 1
                break
            s = flip(0, pos_plus - 1, s)
            ans += 1
        else:
            s = flip(0, pos_neg - 1, s)
            ans += 1

    print("Case #{}: {}".format(tc, ans))
