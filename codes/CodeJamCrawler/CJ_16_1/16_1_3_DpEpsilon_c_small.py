import itertools
n_t = int(raw_input())
for t in xrange(1, n_t+1):
    n = int(raw_input())
    l = [int(x)-1 for x in raw_input().split()]
    done = False
    for y in xrange(n, 0, -1):
        for x in itertools.permutations(range(n), y):
            for i in xrange(y):
                if not (l[x[i]] == x[(i-1)%y] or l[x[i]] == x[(i+1)%y]):
                    break
            else:
                print "Case #{0}: {1}".format(t, y)
                done = True
                break
        if done:
            break
