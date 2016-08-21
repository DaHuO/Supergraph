t = int(raw_input())
for i in xrange(1, t + 1):
    k, c, s = [int(x) for x in raw_input().split(' ')]
    space = 0
    for l in range(c-1):
        space += k * 2**l
    space += 1
    tiles = []
    for j in range(s):
        tiles.append(str(j * space + 1))
    print "Case #{}: {}".format(i, ' '.join(tiles))
