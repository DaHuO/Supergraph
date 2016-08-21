


def solve(N):
    if N == 0: return "INSOMNIA"
    s = set()
    ret = 0
    NN = 0
    while len(s) < 10:
        ret += 1
        NN += N
        for digit in str(NN):
            s.add(digit)
    return NN

tot = int(raw_input())
for caseidx in range(1, tot + 1):
    N = int(raw_input())
    print "Case #%d: %s" % (caseidx, solve(N))
