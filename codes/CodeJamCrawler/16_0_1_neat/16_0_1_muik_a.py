import fileinput
f = fileinput.input()
T = int(f.readline())

def solve(N):
    if N == 0:
        return "INSOMNIA"
    digits = set()
    i = 1
    while (True):
        last_n = N * i
        for n in str(last_n):
            digits.add(n)
        if len(digits) >= 10:
            return last_n
            break
        i += 1
    return N

for case in range(1,T+1):
    N = int(f.readline())
    print "Case #%d: %s" % (case, solve(N))
