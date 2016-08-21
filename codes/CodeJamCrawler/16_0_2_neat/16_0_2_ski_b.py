import sys

outf = None
inf = None


def flip(s, n):
    """
    >>> flip('-+', 1)
    '++'
    >>> flip('+++', 3)
    '---'
    >>> flip('++--', 3)
    '--+-'
    """
    return s[:n].replace('-', 'x').replace('+', '-').replace('x', '+') + s[n:]


def solve(S):
    """
    >>> solve('-+')
    1
    >>> solve('++')
    0
    >>> solve('--+-')
    3
    >>> solve('---+-')
    3
    >>> solve('---+---')
    3
    >>> solve('---+---+')
    3
    >>> solve('---+---+-')
    5
    """
    s = S
    for i in range(len(S)):
        idx = s.rfind('-')
        if idx == -1:
            return i
        s = flip(s, idx + 1)
    return len(S)


def solve_file():
    lines = list(inf)
    assert int(lines[0].strip()) == len(lines[1:])
    for i, case in enumerate(lines[1:], 1):
        print >> outf, 'Case #%d: %s' % (i, solve(case.strip()))


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile.replace('.in', '') + '.out'
    with open(infile) as inf, open(outfile, 'w') as outf:
        solve_file()
