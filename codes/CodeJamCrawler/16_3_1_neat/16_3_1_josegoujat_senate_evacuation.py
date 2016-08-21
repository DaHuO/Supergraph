# Read problem
no_of_cases = int(raw_input())
cases = []
for _ in range(no_of_cases):
    _n = int(raw_input())
    _dist = raw_input().split(' ')
    _dist = [(int(e), chr(65+i)) for i, e in enumerate(_dist)]
    cases.append((_n, _dist))

for i, case in enumerate(cases):
    n, dist = case
    steps = []
    while len(dist) != 0:
        dist = sorted(dist, key=lambda e: e[0], reverse=True)
        if len(dist) == 2:
            if dist[0][0] - dist[1][0] > 1:
                dist[0] = (dist[0][0]-2, dist[0][1])
                steps.append("{}{}".format(dist[0][1], dist[0][1]))
            elif dist[0][0] - dist[1][0] == 1 and dist[1][0] == 1:
                dist[0] = (dist[0][0]-1, dist[0][1])
                steps.append("{}".format(dist[0][1]))
            else:
                dist[0] = (dist[0][0]-1, dist[0][1])
                dist[1] = (dist[1][0]-1, dist[1][1])
                steps.append("{}{}".format(dist[0][1], dist[1][1]))
        else:
            if dist[0][0] >= 2 and dist[0][0] != dist[1][0]:
                dist[0] = (dist[0][0]-2, dist[0][1])
                steps.append("{}{}".format(dist[0][1], dist[0][1]))
            elif len(dist) != 3:
                dist[0] = (dist[0][0]-1, dist[0][1])
                dist[1] = (dist[1][0]-1, dist[1][1])
                steps.append("{}{}".format(dist[0][1], dist[1][1]))
            else:
                dist[0] = (dist[0][0]-1, dist[0][1])
                steps.append("{}".format(dist[0][1]))

        dist = [e for e in dist if e[0] > 0]

    print "Case #{}: {}".format(i+1, " ".join(steps))
