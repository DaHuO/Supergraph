from __future__ import division

def solve(Pi, N):
    ans = []
    total = sum(Pi)
    evacuated = 0

    while evacuated < total:
        first_max = max(Pi)
        first_evac = Pi.index(first_max)
        Pi[first_evac] = Pi[first_evac] - 1
        group = chr(64 + first_evac + 1)
        evacuated = evacuated + 1

        second_max = max(Pi)
        second_evac = Pi.index(second_max)
        maj = (total - evacuated - 1) / 2
        add = True
        for i, p in enumerate(Pi):
            if i != second_evac:
                if p > maj:
                    add = False
                    break

        if add:
            Pi[second_evac] = Pi[second_evac] - 1
            group = group + chr(64 + second_evac + 1)
            evacuated = evacuated + 1

        ans.append(group)

    return ' '.join(ans)

T = int(raw_input())

for x in xrange(1, T + 1):
    N = int(raw_input())
    Pi = [int(s) for s in raw_input().split(' ')]
    y = solve(Pi, N)
    print "Case #{}: {}".format(x, y)