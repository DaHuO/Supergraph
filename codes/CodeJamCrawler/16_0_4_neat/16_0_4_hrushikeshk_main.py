
test = int(raw_input())

for i in range(test):
    k, c, s = raw_input().split()
    tiles = list()

    if k == s:
        for j in range(1, int(k) + 1):
           tiles.append(str(j))
        print "Case #" + str(i+1) + ": " + ' '.join(tiles)
