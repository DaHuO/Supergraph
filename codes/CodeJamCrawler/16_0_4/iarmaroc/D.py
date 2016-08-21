def get_positions(K, C, S):
    KC = pow(K, C-1)
    return [KC * i + 1 for i in xrange(S)]


T = int(raw_input())
for i in xrange(1, T + 1):
    K, C, S = [int(v) for v in raw_input().split(' ')]
    print "Case #{}: {}".format(i, ' '.join([str(p) for p in get_positions(K, C, S)]))
