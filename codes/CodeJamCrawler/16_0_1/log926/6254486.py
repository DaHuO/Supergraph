# https://code.google.com/codejam/contest/dashboard?c=6254486#s=p0
# author: log926

T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    if N == 0:
        print "Case #%d: INSOMNIA" % (i + 1)
        continue

    num = str(N)
    s = set()
    iter = 1
    while len(s) < 10:
        num = str(N * iter)
        nums = map(int, list(num))
        s |= set(nums)
        iter += 1
    print "Case #%d: %s" % (i + 1, num)


