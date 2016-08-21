# Define State
# Pancake 1: happy 0: blank
# Define Action
# Flip at 0 to N - 1
# Answer F(Pancake State i)
# F(S1) = F(S0) + 1 if S0 != S1

T = int(raw_input().strip())


def flipAt(P, i):
    # i = [0, len(P) - 1]
    ret = P[0:i + 1]

    # Reverse ret and flip 0 and 1
    ret = ['0' if p == '1' else '1' for p in reversed(ret)]

    ret.extend(P[i + 1:])

    return ret


def solve(N, src):
    cost = 0
    _src = src[:]
    while True:
        try:
            # Try to find first matched 0
            i = _src.index('0')

            if (i != 0):
                # Flip src such that first i are all zeros
                _src = flipAt(_src, i - 1)
                cost = cost + 1

            # Further flip required no matter all zero or some zeros
            cost = cost + 1

            # Try to find '1'
            i = _src.index('1')

            # Flip _src such that first i are all ones
            _src = flipAt(_src, i - 1)
        except ValueError:
            break

    return cost


for t in xrange(T):
    # Translate - to 0 and + to 1
    Pancakes = ['0' if p == '-' else '1' for p in list(raw_input().strip())]

    # Calculate number of pancakes
    N = len(Pancakes)

    # Solve
    ans = solve(N, Pancakes)

    print 'Case #%d: %d' % (t + 1, ans)
