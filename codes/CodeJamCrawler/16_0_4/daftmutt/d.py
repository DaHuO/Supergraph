import sys

fi = open('D-large.in', 'r')
fo = open('d.out', 'w')

T = int(fi.readline())
    
for t in xrange(T):
    # solve
    line = fi.readline()
    data = line.split()
    K = int(data[0])
    C = int(data[1])
    S = int(data[2])
    
    answer = ''
    if K > S * C:
        answer = 'IMPOSSIBLE'
    else:
        tiles = []
        checked = 0
        while checked < K:
            tile = 0
            if checked + C > K:
                #do K - checked bits
                for i in range(K - checked):
                    tile += (checked + i) * (K**(C-(i + 1)))
            else:
                for i in range(C):
                    tile += (checked + i) * (K**(C-(i + 1)))
            tiles.append(str(tile + 1))
            checked += C
        answer = ' '.join(tiles)
    
    fo.write('Case #{}: {}\n'.format(t + 1, answer))
    print 'Case #{}: {}'.format(t + 1, answer)
    
fi.close()
fo.close()