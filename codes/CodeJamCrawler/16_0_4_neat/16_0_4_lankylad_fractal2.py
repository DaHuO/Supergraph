N = int(raw_input())
for t in xrange(1, N + 1):
    k, c, s = [int(inp) for inp in raw_input().split(' ')]
    first_tile = min(c,k,2)
    last_tile = k
    if last_tile - first_tile + 1 > s:
        print "Case #{}: IMPOSSIBLE".format(t)
        continue
    tiles = range(first_tile,last_tile+1)
    print "Case #{}: {}".format(t, ' '.join(str(tile) for tile in tiles))