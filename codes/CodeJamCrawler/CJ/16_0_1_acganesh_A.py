def validate():
    assert sheep(0) == 'INSOMNIA'
    assert sheep(1) == 10
    assert sheep(2) == 90
    assert sheep(11) == 110
    assert sheep(1692) == 5076
    print 'tests passed!'

def sheep(N):
    if N == 0: return 'INSOMNIA'
    goal = set(map(str, xrange(10)))
    seen = set()
    i = 1

    while seen != goal:
        M = N*i
        s = set(str(M))
        seen = seen.union(s)
        i += 1

    return M


def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        n = int(raw_input())
        print 'Case #%s: %s' % (i, sheep(n))


def test_large():
    print sheep(10**6)
    for N in xrange(10**6+1):
        sheep(N)

#validate()
main()
