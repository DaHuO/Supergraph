for t in range(int(input())):
    l = list(input())
    ans = l[0]
    n = len(l)
    for i in range(1, n):
        if ans[0] <= l[i]:
            ans = l[i] + ans
        else:
            ans += l[i]
    print("Case #" + str(t+1) + ": " + ans)
