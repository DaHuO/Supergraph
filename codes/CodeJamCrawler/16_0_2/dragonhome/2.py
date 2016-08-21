import sys

i = 1


def TestLine(x):
    ii = 0
    buf = x[::-1]
    last_c = 'f'
    # print buf,last_c

    for c in buf:
        if last_c == 'f':
            if c == '-':
                ii += 1
            last_c = c
            continue

        if not (last_c == c):
            ii += 1
            last_c = c

    return ii


f = open('test.tst')
tests_count = f.readline()
while True:
    s = f.readline()
    if s == '':
        break

    r = TestLine(s.strip('\n'))
    print 'Case #%d: %s' % (i, r)
    i += 1



# s = int(f.readline())




