# the negative segment in the beginning takes 1 flip
# all other negative segments takes 2 flips
def solve_helper(s):
    if len(s) == 0:
        return 0
    if s[0] == '+':
        return solve_helper(s[1:])
    else:
        i = 0
        while i < len(s) and s[i] == '-':
            i += 1
        return 2 + solve_helper(s[i:])

def solve(s):
    if s[0] == '-':
        return solve_helper(s) - 1
    else:
        return solve_helper(s)

n = int(raw_input())
for i in range(n):
    s = raw_input()
    print 'Case #%d: %d' % (i+1, solve(s))
