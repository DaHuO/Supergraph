def analysis():
    [k, c, s] = map(int, raw_input().split())
    if s == k:
        return " ".join(map(str, range(1, s + 1)))
    if c == 1:
        return "IMPOSSIBLE"
    return " ".join(map(str, range(2, s + 1)))

cases = int(raw_input())

for i in xrange(cases):
    output = "Case #%i: %s" % (i+1, analysis())
    print output
