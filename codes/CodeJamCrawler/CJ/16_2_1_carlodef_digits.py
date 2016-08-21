def remove_character_from_string(S, x):
    S = list(S)
    for c in S:
        if c == x:
            S.remove(c)
            break
    return ''.join(c for c in S)


def solve(S):
    digits = [('Z', 0, 'ZERO'),
              ('W', 2, 'TWO'),
              ('U', 4, 'FOUR'),
              ('X', 6, 'SIX'),
              ('G', 8, 'EIGHT'),
              ('O', 1, 'ONE'),
              ('H', 3, 'THREE'),
              ('F', 5, 'FIVE'),
              ('S', 7, 'SEVEN'),
              ('I', 9, 'NINE')]
    out = []
    for d in digits:
        for i in xrange(S.count(d[0])):
            out.append(d[1])
            for x in list(d[2]):
                S = remove_character_from_string(S, x)
    return ''.join(str(x) for x in sorted(out))


T = int(raw_input())
for test in xrange(T):
    S = raw_input()
    print "Case #%d: %s" % (test+1, solve(S))
