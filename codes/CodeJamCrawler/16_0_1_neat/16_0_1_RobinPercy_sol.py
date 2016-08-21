# For each N+i, subtract the digits in n+i from a the set of digits left to find
# return the current number when the set bcomes empty

T = int(raw_input())

def solve(c):
    s = set([0,1,2,3,4,5,6,7,8,9])
    N = int(raw_input())
    i = 1

    if N == 0:
        print("Case #%d: INSOMNIA" % c)
        return

    while len(s) > 0:
        n = N * i
        x = set([int(k) for k in str(n) ])
        s -= x
        i += 1

    print("Case #%d: %s" % (c, n))


for i in xrange(1, T+1):
    solve(i)
