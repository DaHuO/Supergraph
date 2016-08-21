inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())
for test in range(1, t + 1):
    p = inf.readline().strip()
    segs = 0
    prev = None
    for c in p:
        if c != prev:
            segs += 1
        prev = c
    if (segs - 1) % 2 == 0:
        if p[0] == '+':
            print('Case #{}: {}'.format(test, segs - 1), file = ouf)
        else:
            print('Case #{}: {}'.format(test, segs), file = ouf)
    else:
        if p[0] == '-':
                print('Case #{}: {}'.format(test, segs - 1), file = ouf)
            else:
                print('Case #{}: {}'.format(test, segs), file = ouf)                
inf.close()
ouf.close()