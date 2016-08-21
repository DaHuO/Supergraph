def solve(m):
    if m == 0:
        return "INSOMNIA"


    b = 1
    s = set()
    while len(s) < 10:
        num = b * m
        for j in str(num):
            s.add(j)

        if len(s) == 10:
            return num


        b += 1


n = int(raw_input())
for i in xrange(n):
    m = int(raw_input())
    ans = solve(m)
    print "Case #{}: {}".format(i + 1, ans)

            