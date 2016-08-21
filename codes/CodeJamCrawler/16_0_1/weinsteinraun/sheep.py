t = int(raw_input())

for case in xrange(t):
    initial_n = int(raw_input())
    n = initial_n
    if n == 0:
        print "CASE #{}: {}".format(case + 1, "INSOMNIA")
        continue
    seen = set()
    seen = set(int(i) for i in str(n))
    while seen != set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
        n += initial_n
        [seen.add(int(i)) for i in str(n)]

    print "Case #{}: {}".format(case + 1, n)
    
