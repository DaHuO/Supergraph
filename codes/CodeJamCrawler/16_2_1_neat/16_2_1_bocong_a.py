from collections import Counter
lst = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
# lst = ['Z', 'ONE', 'W', 'THREE', 'U', 'FV', 'X', 'SV', 'G', 'NN']

def f(s):
    sc = Counter(s)
    ret = ''
    for ni in xrange(len(lst)):
        n = lst[ni]
        nc = Counter(n)
        # print nc, sc
        while all(sc[l] > 0 for l in nc):
            sc = sc - nc
            ret = str(ni) + ret
    return ret

def g(s):
    ret = ''
    uniques = {'Z': 0, 'W': 2, 'U': 4, 'X': 6, 'G': 8}
    sc = Counter(s)
    for k in uniques.keys():
        while k in sc:
            nc = Counter(lst[uniques[k]])
            sc = sc - nc
            ret += str(uniques[k])
    for ni in xrange(len(lst)):
        n = lst[ni]
        nc = Counter(n)
        # print nc, sc
        while all(sc[l] > 0 for l in nc):
            sc = sc - nc
            ret = str(ni) + ret
    return ''.join(sorted(ret))
    

T = int(raw_input())
for t in xrange(1, T + 1):
    s = raw_input()
    print 'Case #{}: {}'.format(t, g(s))