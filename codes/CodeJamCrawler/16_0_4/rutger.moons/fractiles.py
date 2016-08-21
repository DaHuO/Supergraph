__author__ = 'rutger'

def solve(k, c, s):
    if k == 1 and s == 1:
        return [1]
    if c == 1:
        if s == k:
            return range(1, k + 1)
        else:
            return []
    else:
        if s == k:
            return range(2, min(2+k, k+1))
        else:
            return []

def pretty_print(l):
    if len(l) == 0:
        return "IMPOSSIBLE"
    r = ""
    for nb in l:
        r += " " + str(nb)
    return r[1:]


T = int(input())
for t in range(T):
    k, c, s = list(map(int, input().split()))
    result = solve(k, c, s)
    pretty_result = pretty_print(result)
    print("Case #%d: %s" % (t + 1, pretty_result))