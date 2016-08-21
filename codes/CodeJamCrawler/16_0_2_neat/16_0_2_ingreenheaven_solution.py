T = input()

def solve():
    s = raw_input()
    count = 0 if s[0] == '+' else 1
    curr = '+'
    neg_phase = False
    # print s
    for c in s[::-1]:
        # print curr, c
        if curr != c:
            if c == '+':
                count += 2
        curr = c
    return count

for t in range(T):
    ans = solve()
    print 'Case #{0}: {1}'.format(t+1, ans)
