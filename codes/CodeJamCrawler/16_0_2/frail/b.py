INPUT = "2-large"

f = open('%s.in' % INPUT, 'r')
o = open('%s.out' % INPUT, 'w')

T = int(f.readline().strip())


def flip(l2):
    return ['+' if x == '-' else '-' for x in reversed(l2)]


def solve(l, c):
    print l, c

    count_first_pluses = True

    plus_finish = 0
    last_minus = 0

    current_index = 0
    for sign in l:
        current_index += 1
        if sign == '-':
            count_first_pluses = False
            last_minus = current_index
        else:
            if count_first_pluses:
                plus_finish = current_index

    if last_minus == 0:  # no minus left
        return c

    if last_minus == 1:  # only one minus left
        return c + 1

    if last_minus < current_index:
        l = l[:last_minus]

    if plus_finish > 0:  # if there is a plus stuff at start, flip them first
        return solve(flip(l[:plus_finish]) + l[plus_finish:], c+1)

    return solve(flip(l), c+1)

for t in xrange(T):
    total = 0
    inverted = False
    l_s = list(f.readline().strip())
    result = solve(l_s, 0)
    s = "Case #%d: %s\n" % (t+1, result)
    print "----- %d -------" % result
    o.write(s)

f.close()
o.close()
