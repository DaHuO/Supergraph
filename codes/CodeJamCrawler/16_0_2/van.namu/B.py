
def flip(to=-1):
    S_new = ''
    mark = len(S) if to == -1 else to
    for c in S[0:mark]:
        S_new += '+' if c == '-' else '-'

    return S_new[::-1] + S[mark:len(S)]


T = int(raw_input())

for case in range(1, T + 1):
    S = raw_input()
    count = 0

    while '-' in S:
        if '+' in S and S[0] == '+':
            p = S.index('-')
            S = flip(p)
            count += 1
        elif '-' in S and S[0] == '-':
            if '+' in S:
                m = S.index('+')
                S = flip(m)
            else:
                S = flip()
            count += 1

    else:
        print 'Case #%d: %s' % (case, count)