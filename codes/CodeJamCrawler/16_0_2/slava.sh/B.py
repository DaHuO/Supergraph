def solve(s):
    ans = 0
    while True:
        i = s.find('-')
        if i == -1:
            break
        if i != 0:
            ans += 1
            s = '-' * i + s[i:]
        i = s.rfind('-')
        if i == -1:
            break
        ans += 1
        i += 1
        s = ''.join(['+' if c == '-' else '-' for c in s[:i][::-1]]) + s[i:]
    return ans

T = int(input())
for t in range(T):
    s = input()
    ans = solve(s)
    print('Case #{}: {}'.format(t + 1, ans))
