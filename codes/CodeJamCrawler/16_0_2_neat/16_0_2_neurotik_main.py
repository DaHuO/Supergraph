def read_int():
    return int(fi.readline())

def read_intlist():
    return [int(i) for i in fi.readline().split(' ')]

def write_line(i, s):
    fo.write('Case #%d: %s\n' % (i+1, s))

def read_str():
    return fi.readline().strip('\n')

filename = 'B-large'
fi = file(filename + '.in', 'rb')
fo = file(filename + '.out', 'wb')

def flip(pancakes, pos):
    out = ''
    for i in xrange(pos+1):
        out += '-' if pancakes[i] == '+' else '+'
    return out

N = read_int()
for i in xrange(N):
    p = read_str()
    count = 0
    while True:
        pos = p.rfind('-')
        if pos > -1:
            count += 1
            p = flip(p, pos)
        else:
            break

    write_line(i, str(count))




fi.close()
fo.close()