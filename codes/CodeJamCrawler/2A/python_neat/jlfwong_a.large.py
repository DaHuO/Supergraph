"""
There are 9 possible pairs:

PP
PR
PS
RP
RR
RS
SP
SR
SS

Of these, 3 are invalid because they tie, leaving:

PR
PS
RP
RS
SR
SS

Of these, 3 are useless because they're identical to their reverse, but come
lexicographically afterwards, leaving only 3 possible pairs:

PR -> P
PS -> S
RS -> R

So every initial pair AND every eventual matchup must be one of these 3 pairs.
Inspecing the AC response to A small supports this theory.

We don't care about the lexicographical order of the matches beyond the first,
so there's never a reason to choose a matchup where the left half of the
matches comes lexicographically after the right half. This property is
recursively true.

In the largest case, N=12, we have 4096 pairs, or 2048 initial matchups.

For a given N, how many valid answers could there be, ignoring P, R, and S?

For N = 1, there are 3 possible solutions other than IMPOSSIBLE
For N = 2, there are still only 3 possible solutions?

PR <- PRRS
PS <- PRPS
RS <- RSPS

And this is deterministically true recursively! So all we have to do is produce
the 3 solutions for each given N, and see if any of them match the provided P,
S, and R
"""

from collections import Counter

T = input()

def winner_to_match(x):
    if x == 'P':
        return 'PR'
    if x == 'S':
        return 'PS'
    if x == 'R':
        return 'RS'

    assert False, x

def expand(matchlist, N):
    if N == 0:
        return matchlist

    return expand(''.join(winner_to_match(x) for x in matchlist), N-1)

def optimized(matchlist):
    if len(matchlist) < 2:
        return matchlist

    halflen = len(matchlist) / 2

    left = optimized(matchlist[:halflen])
    right = optimized(matchlist[halflen:])

    if left < right:
        return left + right
    else:
        return right + left

for case_num in xrange(T):
    N, R, P, S = map(int, raw_input().split())

    ans = 'IMPOSSIBLE'

    for victor in ('R', 'P', 'S'):
        expanded = expand(victor, N)
        counts = Counter(expanded)
        if counts['R'] == R and counts['P'] == P and counts['S'] == S:
            ans = optimized(expanded)
            break

    print 'Case #%d: %s' % (case_num + 1, ans)
