for y in range(int(input())):

    s = input()
    ans = s[0]

    for i in s[1:]:

        if ord(i) >= ord(ans[0]):
            ans = i + ans
        else:
            ans += i

    print("Case #%d: %s" %(y+1, ans))
