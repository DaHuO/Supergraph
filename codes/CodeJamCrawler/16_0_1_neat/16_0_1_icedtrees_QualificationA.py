t = int(raw_input())
for c in range(t):
    n = int(raw_input())
    d = set()
    if n == 0:
        result = "INSOMNIA"
    else:
        k = 1
        while len(d) < 10:
            d |= set(str(k * n))
            k += 1
        result = (k - 1) * n
    print "Case #{}: {}".format(c+1, result)