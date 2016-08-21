from sys import argv

def get_tiles(K, C, S):
    if K <= S:
        tiles = range(1, S+1)
    else:
        return 'IMPOSSIBLE'

    return ' '.join([str(t) for t in tiles])

if __name__=='__main__':

    fin = open(argv[1], 'r')
    tnum = int(fin.readline())
    fout = open(argv[1]+'_out', 'w')

    for i, l in enumerate(fin, 1):
        params = [int(p) for p in l.split()]
        fout.write('Case #{0}: {1}\n'.format(i, get_tiles(params[0], params[1], params[2])))
