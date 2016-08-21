__author__ = 'snv'
f = open('B-large.in','r')
g = open('output.txt', 'w')
n = int(f.readline())
for j in range(n):
    a = f.readline().strip()
    lngth = len(a)
    if a[-1] == '-':
        groups = 1
    else:
        groups = 0

    cur = a[0]
    start = 1
    while start<lngth:
        if a[start] != cur:
            cur = a[start]
            groups += 1
        start += 1
    print('Case #{0}: {1}\n'.format(j+1, groups))
    g.write('Case #{0}: {1}\n'.format(j+1, groups))
f.close()
g.close()

