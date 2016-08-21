def solve(s):
    cnt = 0
    mem = s[0]
    for c in s[1:]:
        if c != mem:
           cnt += 1
           mem = c
    if mem == '-':
        cnt += 1
    return cnt


T = int(raw_input())
for i in xrange(1, T+1):
    S = raw_input()
    print 'Case #' + str(i) + ': ' + str(solve(S))
