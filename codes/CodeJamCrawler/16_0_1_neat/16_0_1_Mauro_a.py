def read_int():
    return int(raw_input())

def solve(N):
    if N == 0:
        return "INSOMNIA"
    seen = set()
    n = 0
    while True:
        n += N
        ans = n
        seen.update(set(str(n)))
        if len(seen) == 10:
            return ans

for case in range(read_int()):
    N = read_int()
    ans = solve(N)
    print "Case #%d: %s" % (case+1, ans)
