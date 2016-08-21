for t in range(int(input())):
    ans=""
    s=input()
    for i in s:
        if not ans:
            ans+=i
        else:
            if ord(i)<ord(ans[0]):
                ans+=i
            else:
                ans = i+ans
    print("Case #{}: {}".format(t+1,ans))