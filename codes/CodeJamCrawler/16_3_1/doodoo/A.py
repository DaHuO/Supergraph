def solve(Ps):
    S = sum(Ps)

    ret = ''

    while S > 0:
        M = max(Ps)
        assert 2*M <= S


        if ret != '':
            ret += ' '

        if Ps[0] > Ps[1]:
            m = 0
            n = 1
        else:
            m = 1
            n = 0

        for i, p in enumerate(Ps):
            if i < 2:
                continue
            if Ps[i] > min(Ps[m], Ps[n]):
                if Ps[i] > Ps[m] and Ps[i] > Ps[n]:
                    m = i
                    n = m
                else:
                    n = i

        if S % 2 == 0:
            # Try removeing 1 from M
            M = 0
            for i, p in enumerate(Ps):
                P = p
                if i == m:
                    P = max(0, p - 2)
                if P > M:
                    M = P

            if 2*M <= S - 2:
                ret += chr(ord('A') + m) + chr(ord('A') + m)
                Ps[m] = Ps[m] - 2
                S -= 2
                continue
        else:
            # Try removeing 1 from M
            M = 0
            for i, p in enumerate(Ps):
                P = p
                if i == m:
                    P = max(0, p - 1)
                if P > M:
                    M = P

            if 2*M <= S - 1:
                ret += chr(ord('A') + m)
                Ps[m] = Ps[m] - 1
                S -= 1
                continue


        ret += chr(ord('A') + m) + chr(ord('A') + n)
        Ps[m] = Ps[m] - 1
        Ps[n] = Ps[n] - 1
        S -= 2

    return ret


T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    Ps = [int(x) for x in raw_input().split()]

    print 'Case #%d: %s' % (i + 1, solve(Ps))
