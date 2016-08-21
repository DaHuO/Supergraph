def read_int():
    return int(fi.readline())

def read_intlist():
    return [int(i) for i in fi.readline().split(' ')]

def write_line(i, s):
    line = 'Case #%d: %s\n' % (i+1, s)
    if debug: print line
    fo.write(line)

def read_str():
    return fi.readline().strip('\n')

debug = False
filename = 'A-large'
fi = file(filename + '.in', 'rb')
fo = file(filename + '.out', 'wb')

def seen_all(s):
    nums = '0123456789'
    for num in nums:
        if not num in seen:
            return False
    return True


T = read_int()
for i in xrange(T):
    n = read_int()
    j = 0
    seen = ''
    while True:
        j += 1
        if n == 0:
            write_line(i, 'INSOMNIA')
            break
        else:
            seen += str(n*j)
            if seen_all(seen):
                write_line(i, str(n*j))
                break





fi.close()
fo.close()