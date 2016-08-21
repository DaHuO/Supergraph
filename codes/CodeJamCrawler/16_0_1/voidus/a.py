import sys
import json

def sleep(N):
    digits = {0,1,2,3,4,5,6,7,8,9}
    c = N
    enc = set()
    while True:
        enc |= set(map(int, str(c)))
        if enc == digits:
            break
        c += N
        #print 'c=', c, 'digits', enc
    return c

if __name__ == '__main__':
    with open('precomputed.txt', 'rb') as precomputed:
        hashmap = dict(json.load(precomputed))
    with open(sys.argv[1], 'rb') as ok:
        ok.readline()
        for index, line in enumerate(ok):
            line = line.strip()
            if line:
                print 'Case #%d: %s' % (index+1, hashmap.get(int(line), 'INSOMNIA'))
