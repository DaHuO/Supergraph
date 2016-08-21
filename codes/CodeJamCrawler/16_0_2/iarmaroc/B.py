def solve(pancakes):
    changes = 0
    last = pancakes[0]
    for p in pancakes:
        if p != last:
            changes += 1
        last = p

    stack_size = changes + 1
    if stack_size % 2:
        if pancakes[0] == '+':
            return changes
        return changes + 1

    if pancakes[0] == '+':
        return changes + 1
    return changes


T = int(raw_input())
for t in xrange(1, T+1):
    p = raw_input()
    print "Case #{}: {}".format(t, solve(p))
