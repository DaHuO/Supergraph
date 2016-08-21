import sys

f = open(sys.argv[1], 'r')
T = int(f.readline().strip())

for t in xrange(T):
    N = int(f.readline().strip())
    if N == 0:
        print "Case #{0}: {1}".format(t+1, "INSOMNIA")
        continue

    count = 1
    seen  = map(int, set(str(N)))
    while list(set(seen)) != range(10):
        count += 1
        seen.extend(map(int, set(str(N * count))))

    print "Case #{0}: {1}".format(t+1, N * count)