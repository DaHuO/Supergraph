def factiles(K, C, S):
    minS = (K + 1) / 2
    if (C == 1 and S < K) or S < minS:
        return "IMPOSSIBLE"
    if C == 1:
        return ' '.join([str(i) for i in xrange(1, K + 1)])
    unit = K**(C - 1)
    pick = -2*unit
    seq = []
    for i in xrange(1, K / 2 + 1):
        pick += 2*unit + 2
        seq.append(str(pick))
    if K % 2 == 1:
        seq.append(str(K*unit))
    return ' '.join(seq)

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        K, C, S = [int(s) for s in raw_input().split(" ")]
        print 'Case #{}: {}'.format(i, factiles(K, C, S))
