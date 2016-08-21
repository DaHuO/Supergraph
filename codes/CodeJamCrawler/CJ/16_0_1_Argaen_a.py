
def solve(n):
    if n == 0:
        return 'INSOMNIA'
    found = [False]*10
    i = 1
    while not all(found):
        t = n*i
        while t:
            found[t%10] = True
            t /= 10
        i += 1
    return n * (i - 1)

T = int(raw_input())
i = 1
while i <= T:
    n = int(raw_input())
    print 'Case #{0}: {1}'.format(i, solve(n))
    i += 1

