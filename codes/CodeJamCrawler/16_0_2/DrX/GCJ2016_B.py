for ca in xrange(input()):
    s = raw_input()
    n, i, cnt = len(s), 0, 0
    while i < n:
        j = i + 1
        while j < n and s[i] == s[j]:
            j += 1
        cnt += 1
        i = j

    if s[-1] == '+':
        cnt -= 1
    print "Case #" + str(ca + 1) + ":", cnt
