import sys

sys.setrecursionlimit(10**6)

for i, s in enumerate(sys.stdin.read().split()[1:]):
    priority = sorted(((b, a) for a, b in enumerate(s)))
    ans = []
    
    def solve(l):
        if not priority:
            return
        cur = priority[-1][1]
        while priority and priority[-1][1] >= cur:
            priority.pop()
        ans.append(s[cur])
        solve(cur)
        ans.append(s[cur+1:l])
    
    solve(len(s))
    print('Case #{}: {}'.format(i + 1, ''.join(ans)))