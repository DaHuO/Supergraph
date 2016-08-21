import os

fp = open('A-large.in')
of = open('lalala-large','w')
s = fp.readline()
cnt = 0
all = set('0123456789')
while True:
    s = fp.readline()
    cnt += 1
    try:
        start = int(s)
    except:
        of.close()
        os._exit(0)

    factor = 1
    num = set(str(start))

    if start == 0:
        print >>of, 'Case #%d: INSOMNIA' % cnt
        continue

    while not num.issuperset(all) :
        factor += 1
        m = start * factor
        num.update(str(m))

    print >>of,'Case #%d: %d' % (cnt, m)


