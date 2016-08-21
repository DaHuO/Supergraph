def case(s1, s2):
    if s1 == '-' and s2 == '+':
        return 1
    elif s1 == '+' and s2 == '-':
        return 2
    elif s1 == '+' and s2 == '+':
        return 0
    elif s1 == '-' and s2 == '-':
        return 1
    else:
        raise Exception('Not expecting s1 = %s and s2 = %s' % (s1, s2))

def solution(s):

    if len(s) == 1:
        return 1 if s[0] == '-' else 0
    else:
        g = [s[0]]
        for x in s[1:]:
            if g[-1] != x:
                g.append(x)
        if len(g) == 1:
            return 1 if g[0] == '-' else 0

        count = case(g[0], g[1])
        for x in g[2:]:
            if x == '-':
                count += 2

        return count


with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            x = solution(line.strip('\n'))
            print "Case #{}: {}".format(i, x)

