digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def get_number(S, n):
    if S == '':
        return ''

    if all(x in S for x in digits[n]):
        for c in digits[n]:
            S = S.replace(c, '', 1)

        for i in xrange(10):
            a = get_number(S, i)
            if a is not None:
                return str(n) + a
    return None

T = int(raw_input())


for case in xrange(1, T+1):
    S = raw_input()

    for i in xrange(10):
        ans = get_number(S, i)

        if ans is not None:
            break

    ans = ''.join(sorted(ans))

    print 'Case #{}: {}'.format(case, ans)
