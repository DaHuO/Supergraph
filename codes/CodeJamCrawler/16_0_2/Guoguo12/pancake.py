IN = 'B-small-attempt2.in'
OUT = IN.split('.')[0] + '.out'

def good(stack):
    if len(stack) == 0:
        return True
    return all(c == '+' for c in stack)

def flip(stack):
    s = ''
    for c in reversed(stack):
        s += '+' if c == '-' else '-'
    return s

memo = {}
def solve(stack):
    if stack in memo:
        return memo[stack]

    done = {}
    queue = [(stack, 0)]
    seen = set()
    while len(queue) > 0:
        front, depth = queue.pop(0)
        seen.add(front)
        if good(front):
            memo[stack] = depth
            return depth

        children = []
        for i in xrange(len(front)):
            children.append(flip(front[:i+1]) + front[i+1:])
        for c in children:
            if c not in seen:
                queue.append((c, 1 + depth))
    return -1

stacks = [s.strip() for s in filter(lambda x: x, open(IN).read().split('\n'))[1:]]
l = len(stacks)
open(OUT, 'w')
for i, stack in enumerate(stacks):
    if i % 10 == 0:
        print 'On %d of %d' % (i + 1, l)
    print >>open(OUT, 'a'), 'Case #%d: %s' % (i + 1, solve(stack))
