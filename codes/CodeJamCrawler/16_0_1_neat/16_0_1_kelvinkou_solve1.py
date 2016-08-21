def update(curr, seen):
    digits = set(str(curr))
    for x in xrange(10):
        if str(x) in digits:
            seen[x] = 1
    return seen


def solve(n):
    if n == 0:
        return 'INSOMNIA'
    i = 1
    seen = [0] * 10
    while not all(seen):
        curr = n * i
        seen = update(curr, seen)
        i += 1
    return curr

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, solve(n))
