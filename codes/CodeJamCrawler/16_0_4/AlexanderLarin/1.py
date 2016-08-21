fi = open('input')
fo = open('output', 'w')

T = int(fi.readline())

for Ti in range(1, T + 1):
    l = fi.readline().strip().split(' ')
    K = int(l[0])
    C = int(l[1])
    S = int(l[1])

    print("Case #%d: " % Ti, end=' ')
    for i in range(1, K + 1):
        print("%d" % i, end=' ')
    print()

fi.close()
fo.close()
