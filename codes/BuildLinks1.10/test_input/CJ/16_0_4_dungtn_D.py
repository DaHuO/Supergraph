import sys


def gen_tiles(K, C):
    tiles = ['G'] * K
    for i in xrange(C):
        for piece in tiles:
            if piece == "L":
                pass
            else:
                pass
def main():
    f = open(sys.argv[1], 'r')
    T = int(f.readline().strip())

    for t in xrange(T):
        K, C, S = map(int, f.readline().strip().split(' '))
        print "Case #{0}: {1}".format(t+1, " ".join(str(x) for x in xrange(1, K+1)))


if __name__=="__main__":
    main()