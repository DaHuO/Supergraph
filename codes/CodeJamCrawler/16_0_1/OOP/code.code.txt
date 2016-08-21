def solve():
    s=input()
    ans=s[0]
    for i in s[1:]:
        if ord(ans[0])<=ord(i):
            ans=i+ans
        else:
            ans=ans+i
    print(ans)
if __name__ == "__main__":
    for i in range(int(input())):
        print("Case #%d: "%(i+1),end='')
        solve()