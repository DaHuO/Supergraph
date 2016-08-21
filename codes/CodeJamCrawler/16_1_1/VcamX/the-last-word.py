
def solve(s):
    ans = [s[0]]
    for ch in s[1:]:
        if ord(ch) >= ord(ans[0]):
            ans.insert(0, ch)
        else:
            ans.append(ch)
    return ''.join(ans)

t = int(input())
for i in range(1, t + 1):
    s = input()
    print("Case #{}: {}".format(i, solve(s)))

