


cases = input()
for case in xrange(cases):
    bool_map = [False for i in xrange(10)]

    N = input()
    i = 1
    if N == 0:
        print("Case #{}: INSOMNIA".format(case + 1))
    else:
        while(not all(bool_map)):
            r = N * i
            for a in str(r):
                bool_map[int(a)] = True
            i += 1
        print("Case #{}: {}".format(case + 1, r))
