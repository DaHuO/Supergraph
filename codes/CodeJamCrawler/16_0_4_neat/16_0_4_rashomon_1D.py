test = int(input())
for i in range(test):
    k, c, s = map(int, input().split())
    cnt = 0
    ans = []
    if c == 1:
        cnt = k
        ans = range(1, k + 1)
    elif c < k:
        cnt = k - c + 1
        ans = range(1, k + 1)
    else:
        cnt = 1
        if k > 1:
            ans = [(k**k - k) // ((k - 1)**2)]
        else:
            ans = [1]
    if (s < cnt):
        print("Case #%d: IMPOSSIBLE" % (i + 1))
    else:
        print("Case #%d: " % (i + 1), end="")
        for e in ans:
            print(e, end=' ')
        print()