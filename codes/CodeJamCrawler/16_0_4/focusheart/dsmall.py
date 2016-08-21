from bitarray import bitarray
from itertools import product

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        k, c, s = [int(s) for s in raw_input().split(" ")]
        ppos = get_positions(k, c, s)
        print "Case #{}: {}".format(i, ' '.join(ppos))

def get_positions(k, c, s):
    # if k==s is True, you can always know the origin pattern
    ppos = map(str, range(1, s+1))
    return ppos

def gen_pattern(k, c):
    ptns = list(product('GL', repeat=k))
    for ptn in ptns:
        o = ''.join(ptn)
        s = ''.join(ptn)
        for i in range(c-1):
            s = s.replace('G', 'G'*k)
            s = s.replace('L', o)
        print o, s

if __name__=='__main__':
    main()
