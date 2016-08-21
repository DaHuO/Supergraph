def o(c):
    if c == '+':
        return '-'
    return '+'


def solve(s):
    cost = {'+': 0, '-': 0}
    for c in s:
        newcost = {}
        cost[o(c)] = cost[c]+1
        #print cost
    return cost['+']


if __name__ == '__main__':
    import sys
    T = int(sys.stdin.readline())
    for case in range(T):
        s = sys.stdin.readline()
        n = solve(s.strip())
        print 'Case #%d: %d' % (case+1, n)

