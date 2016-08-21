T = input()

for t in xrange(1, T+1):
    line = raw_input().split(" ")
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    totalTiles = K**C
    tilesRatio = totalTiles/K

    print "Case #"+str(t)+":", " ".join([str(x) for x in xrange(1, totalTiles+1, tilesRatio)])