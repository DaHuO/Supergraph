import sys

outf = None
inf = None


def solve(K, C, S):
    """
    >>> print solve(4, 3, 4)
    7 64
    >>> print solve(5, 3, 4)
    8 100
    >>> print solve(2, 3, 2)
    4
    >>> print solve(1, 1, 1)
    1
    >>> print solve(3, 1, 2)
    IMPOSSIBLE
    >>> print solve(3, 2, 2)
    2 9
    >>> print solve(4, 2, 2)
    2 12
    >>> print solve(10, 2, 10)
    2 24 46 68 90
    """
    kc = K ** C
    if S * C < K:
        return 'IMPOSSIBLE'
    result = []
    for s in range(1, S+1):
        p = 0
        for x in range(1, C):
            p += ((s-1)*C+x-1)*(K**(C-x))
        sc = min(s * C, K)
        p += sc
        p = min(p, kc)
        assert p <= kc, p
        result.append(p)
        if sc == K:
            break
    if K ** C < 10000000:
        validate(K, C, S, result)
    return ' '.join(map(str, result))


def validate(K, C, S, answer):
    """
    >>> validate(3, 1, 1, [1])
    Traceback (most recent call last):
        ...
    AssertionError: Not a valid answer
    >>> validate(3, 3, 2, [1, 2])
    Traceback (most recent call last):
        ...
    AssertionError: Not a valid answer
    """
    assert K ** C < 10000000
    assert len(answer) <= S
    assert len(answer) == len(set(answer))
    combs = [('L' * i + 'G' + 'L' * (K-i-1)) for i in range(K)]
    for pattern in combs:
        assert len(pattern) == K
        s = pattern
        for i in range(C):
            s = s.replace('G', 'G' * K).replace('L', pattern)
        assert any(
            s[p-1] == 'G' for p in answer
        ), ('Not a valid answer', K, C, S, answer, 'for', pattern)


def solve_file():
    lines = list(inf)
    assert int(lines[0].strip()) == len(lines[1:])
    for i, case in enumerate(lines[1:], 1):
        K, C, S = map(int, case.strip().split())
        if S == K:  # silly fast
            result = ' '.join(map(str, range(1, S+1)))
        else:
            result = solve(K, C, S)
        print >> outf, 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile.replace('.in', '') + '.out'
    with open(infile) as inf, open(outfile, 'w') as outf:
        solve_file()
