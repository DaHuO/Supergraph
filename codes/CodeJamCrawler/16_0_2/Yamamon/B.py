T = int(raw_input())

def flip(s):
    s = ['-' if c == '+' else '+' for c in s]
    s.reverse()
    return ''.join(s)

for case in xrange(1, T+1):
    S = raw_input().rstrip('+')
    result = 0
    while S:
        result += 1
        if S[0] == '-':
            S = flip(S)
        else:
            j = S.index('-')
            S = flip(S[0:j]) + S[j:]
        S = S.rstrip('+')
    print 'Case #%d: %s' % (case, result)
