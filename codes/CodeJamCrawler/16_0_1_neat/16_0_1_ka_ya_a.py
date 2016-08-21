def solve(n):

    if n == 0:
        return 'INSOMNIA'

    check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 1
    while True:
        digits = str(i*n)
        for c in digits:
            check[int(c)] = 1
        if sum(check) == 10:
            return str(i*n)
        i += 1


T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    print 'Case #' + str(i+1) + ': ' + solve(N)
