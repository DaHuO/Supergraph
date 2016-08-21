#!/usr/bin/env python2
forbidden_child_ = {
    'RP': None,
    'PR': 'P',
    'PS': None,
    'SP': 'S',
    'SR': None,
    'RS': 'R',
}
def forbidden_child(winner, other):
    return forbidden_child_[winner + other]

winner = {
    'RP': 'P',
    'PR': 'P',
    'PS': 'S',
    'SP': 'S',
    'RS': 'R',
    'SR': 'R',
}

def combine(x, y):
    if None in (x, y):
        return None
    return winner.get(x + y, 'ERROR')

def main():
    for t in xrange(1, 1 + int(raw_input())):
        print 'Case #%d:' % t,
        N, R, P, S = map(int, raw_input().split())
        amt = {'P': P, 'R': R, 'S': S}
        ans = [None] * ((1 << (N + 1)) + 1)
        last = 1 << N

        def update(i, x):
            assert 0 <= i < (1 << N)
            j = last + i
            while j != 0:
                y = combine(x, ans[j ^ 1])
                if y == 'ERROR':
                    return False
                ans[j] = x
                x = y
                j /= 2
            return True

        def assign(i, x):
            if i == (1 << N):
                return True

            if amt[x] == 0:
                return False

            #print 'assign', i, x, amt, ans[last:last + (1 << N)]
            amt[x] -= 1
            if update(i, x):
                for x2 in 'PRS':
                    if assign(i + 1, x2):
                        return True
                update(i, None)
                #print 'unassign', i, x, amt, ans[last:last + (1 << N)]
            amt[x] += 1
            return False

        def solve():
            for x in 'PRS':
                if assign(0, x):
                    return True

        if solve():
            print ''.join(ans[last:last + (1 << N)])
        else:
            print 'IMPOSSIBLE'

if __name__ == '__main__':
    main()
