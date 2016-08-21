'''
Senate Evacuation
'''
if __name__ == '__main__':
    T = int(raw_input())
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in xrange(1, T + 1):
        N = int(raw_input())
        P = [int(s) for s in raw_input().split(" ")]
        c = sum(P)
        x = ''
        while c > 0:
            m1 = 0
            m2 = 0
            j1 = 0
            j2 = 0
            for j in xrange(N):
                if P[j] >= m1:
                    m2 = m1
                    j2 = j1
                    m1 = P[j]
                    j1 = j
            #print m1, m2
            if sum(P) == 3:
                P[j1] -= 1
                x += al[j1] + ' '
            else:
                if m1 - m2 > 1:
                    P[j1] -= 2
                    x += al[j1] + al[j1] + ' '
                else:
                    P[j1] -= 1
                    P[j2] -= 1
                    x += al[j1] + al[j2] + ' '
            c -= 2
        x = x.rstrip()
        print "Case #{}: {}".format(i, x)
