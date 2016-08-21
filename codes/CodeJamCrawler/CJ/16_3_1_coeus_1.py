import sys

def emptying(Ps, bal):
    output = []
    max_pair = 0
    for p in Ps:
        if p in bal: 
            max_pair = p[1]
            continue
        pairs = p[1]/2
        single = p[1] % 2
        output.extend(["%s%s" % (p[0], p[0])] * pairs)
        if single == 1:
            output.append("%s" % p[0])

    max_str = "".join(p[0] for p in bal)
    output.extend(["%s" % max_str] * max_pair)
    return output

def balance_max(Ps):
    counts = sorted(Ps, key = lambda dt: dt[1], reverse=True)
    if len(counts) > 1:
        max1 = counts[0][1]
        max2 = counts[1][1]
        diff = max1 - max2
        for i in range(len(Ps)):
            if Ps[i][0] == counts[0][0]:
                Ps[i] = (counts[0][0], counts[1][1])
        if diff == 1:
            return counts[0][0]
        elif diff ==2:
            return "%s%s" % (counts[0][0], counts[0][0])
    return ""


def get_maxes(Ps):
    Ps_max = max([p[1] for p in Ps])
    Ps_max_count = [p for p in Ps if p[1] == Ps_max]
    return Ps_max, Ps_max_count

def solve(N, P):
    Ps = [(str(unichr(ord('A') + i)), p) for i, p in enumerate(P)]
    Ps_max, Ps_max_count = get_maxes(Ps)

    if len(Ps_max_count) >= 2:
        bal = Ps_max_count[:2]
        return emptying(Ps, bal)
    else:
        output = [balance_max(Ps)]
        Ps_max, Ps_max_count = get_maxes(Ps)
        bal = Ps_max_count[:2]
        output += emptying(Ps, bal)
        return output

t = raw_input().strip()
t = int(t)

for x in range(t):
    N = int(raw_input().strip())
    P = [int(p) for p in raw_input().strip().split(" ")]
    print "Case #%d: %s" % (x + 1, " ".join(solve(N, P)))
