def f(n):
    a = {str(x): 0 for x in range(0, 10)}
    i = 0
    while(1):
        i += 1
        curr_n = i * n
        for x in str(curr_n):
            a[x] += 1
        if all(v != 0 for k, v in a.items()):
            return curr_n

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())

    if n == 0:
        print "Case #{}: INSOMNIA".format(i)
        continue

    print "Case #{}: {}".format(i, f(n))
