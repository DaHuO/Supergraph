T = int(raw_input())
for tc in xrange(1, T + 1):
    R, C = map(int, raw_input().split())
    courtiers = map(int, raw_input().split())

    def solve():
        for perm_i in xrange(1 << R * C):
            cells = ['/' if (1 << i) & perm_i else '\\' for i in xrange(R * C)]

            for i in xrange(R + C):
                a = courtiers[2 * i]
                b = courtiers[2 * i + 1]
                if a <= C:
                    x, y = a - 1, 0
                    dx, dy = 0, 1
                elif a <= C + R:
                    x, y = C - 1, a - C - 1
                    dx, dy = -1, 0
                elif a <= C + R + C:
                    x, y = C + R + C - a, R - 1
                    dx, dy = 0, -1
                else:
                    x, y = 0, 2 * (R + C) - a
                    dx, dy = 1, 0

                while 0 <= x < C and 0 <= y < R:
                    if cells[C * y + x] == '/':
                        if (dx, dy) == (1, 0):
                            dx, dy = (0, -1)
                        elif (dx, dy) == (-1, 0):
                            dx, dy = (0, 1)
                        elif (dx, dy) == (0, 1):
                            dx, dy = (-1, 0)
                        else:
                            dx, dy = (1, 0)
                    else:
                        if (dx, dy) == (1, 0):
                            dx, dy = (0, 1)
                        elif (dx, dy) == (-1, 0):
                            dx, dy = (0, -1)
                        elif (dx, dy) == (0, 1):
                            dx, dy = (1, 0)
                        else:
                            dx, dy = (-1, 0)
                    x += dx
                    y += dy

                if y == -1:
                    t = 1 + x
                elif x == C:
                    t = C + 1 + y
                elif y == R:
                    t = C + R + C - x
                else:
                    t = 2 * (R + C) - y

                if b != t:
                    break
            else:
                lines = []
                for i in xrange(R):
                    lines.append(''.join(cells[C * i:C * (i + 1)]))
                return '\n'.join(lines)
        return 'IMPOSSIBLE'

    print 'Case #{}:\n{}'.format(tc, solve())
