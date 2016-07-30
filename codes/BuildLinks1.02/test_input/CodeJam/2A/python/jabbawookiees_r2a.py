requirements = {
    'P': 'PR',
    'R': 'RS',
    'S': 'PS'
}


def solve(winner, level):
    if level == 0:
        return winner
    else:
        req = requirements[winner]
        left = memoized_solve(req[0], level - 1)
        right = memoized_solve(req[1], level - 1)
        if left < right:
            return left + right
        else:
            return right + left

cache = {}


def memoized_solve(winner, level):
    if cache.get((winner, level)) is None:
        soln = solve(winner, level)
        cache[winner, level] = soln
    return cache[winner, level]


def is_valid(sol, r, p, s):
    counter = {
        'R': 0,
        'P': 0,
        'S': 0,
    }
    for c in sol:
        counter[c] += 1
    if counter['R'] == r and counter['P'] == p and counter['S'] == s:
        return True
    return False

cases = int(raw_input())
for ctr in xrange(cases):
    n, r, p, s = [int(x) for x in raw_input().split(" ")]
    solp = memoized_solve('P', n)
    solr = memoized_solve('R', n)
    sols = memoized_solve('S', n)
    solns = [sol for sol in [solr, sols, solp] if is_valid(sol, r, p, s)]

    if solns:
        soln = min(solns)
    else:
        soln = None

    if not soln:
        soln = 'IMPOSSIBLE'

    print "Case #%d: %s" % (ctr + 1, soln)
