import sys

def getTiles(K,C,S):
    # small input set, we have enough workers to check all tiles
    if S==K:
        offset = K**(C-1)
        tiles = range(1,K**C+1,offset)
        for i in range(len(tiles)):
            tiles[i] = str(tiles[i])
        return ' '.join(tiles)

if __name__ == "__main__":
    f = open(sys.argv[1],'r')
    T = int(f.readline())
    for i in xrange(1,T+1):
        [K,C,S] = f.readline().split()
        K=int(K)
        C=int(C)
        S=int(S)
        print "Case #" + str(i) + ": " + getTiles(K,C,S)
    f.close()
