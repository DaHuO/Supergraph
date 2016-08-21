def solve(st):
    st = [st[0]] + [st[index] for index in range(1, len(st)) if st[index] != st[index - 1]]
    ans = len(st)
    if st[-1] == '+':
        ans -= 1
    return ans

T = input()
for t in range(T):
    print "Case #%s: %s " % (t + 1,solve(raw_input()))
