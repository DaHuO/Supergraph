import math
import sys

def get_tiles_to_clean(K, C, S):
    kc1 = int(math.pow(K, C-1))
    return [(i * kc1) + 1 for i in xrange(S)]

T = int(sys.stdin.readline())
for t in xrange(T):
    (K, C, S) = [int(x) for x in sys.stdin.readline().split()]
    tiles = get_tiles_to_clean(K, C, S)
    print 'Case #' + str(t+1) + ': ' + (' '.join(map(str, tiles)) if tiles else 'IMPOSSIBLE')

