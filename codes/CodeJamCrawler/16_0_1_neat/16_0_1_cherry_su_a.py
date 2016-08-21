def solve_slow(N, seen_zero=False):
    s = set() if not seen_zero else set(['0'])
    for k in range(1, 75):
        for d in str(k*N):
            s.add(d)
        if len(s) == 10:
            return str(k*N)
    assert False, "wtf"

def solve(N, seen_zero=False):
    if N == 0:
        return "INSOMNIA"

    last_digit = N % 10
    if last_digit in (1, 3, 7, 9):
        s = set() if not seen_zero else set(['0'])
        for k in range(1, 11):
            for d in str(k*N):
                s.add(d)
            if len(s) == 10:
                return str(k * N)
        assert False, "this shouldn't happen"
    elif last_digit == 0:
        N2 = N
        p = 0
        while N2 % 10 == 0:
            N2 /= 10
            p += 1
        return str(int(solve(N2, seen_zero=True)) * 10**p)
    else:
        return solve_slow(N, seen_zero)

if '__main__' == __name__:
    T = int(raw_input())
    for _t in range(1, T+1):
        N = int(raw_input())
        print "Case #%d: %s" % (_t, solve(N))
