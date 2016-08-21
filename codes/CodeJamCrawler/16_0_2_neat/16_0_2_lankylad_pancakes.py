o = ['+', '-']

def flip_pancakes(p, x):
    f = p[x - 1::-1]
    f = ''.join([o[i == '+'] for i in f])
    p = f + p[x:]
    return p

def count_same(p):
    first = p[0]
    c = 0
    while c < len(p) and p[c] == first:
        c += 1
    return c


if __name__ == '__main__':
    N = int(raw_input())
    for t in xrange(1,N+1):
        pancakes = raw_input()
        n = 0
        while '-' in set(pancakes):
            x = count_same(pancakes)
            pancakes = flip_pancakes(pancakes, x)
            n += 1
        print "Case #{}: {}".format(t, n)



