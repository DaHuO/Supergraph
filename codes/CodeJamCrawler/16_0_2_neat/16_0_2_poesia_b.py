T = int(input())

for i in range(1, T+1):
    s = input()
    while len(s) and s[-1] == '+':
        s = s[:-1]
    last = None
    ans = 0
    for c in s:
        if c != last:
            ans += 1
        last = c
    print("Case #{}: {}".format(i, ans))

