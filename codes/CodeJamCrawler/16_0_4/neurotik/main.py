def read_int():
    return int(fi.readline())

def read_intlist():
    return [int(i) for i in fi.readline().split(' ')]

def write_line(i, s):
    line = 'Case #%d: %s\n' % (i+1, s)
    #print line
    fo.write(line)

def read_str():
    return fi.readline().strip('\n')

filename = 'D-small-attempt1'
fi = file(filename + '.in', 'rb')
fo = file(filename + '.out', 'wb')


T = read_int()
for i in xrange(T):
    K, C, S = read_intlist()

    if C == 1:
        if S < K:
            write_line(i, 'IMPOSSIBLE')
        else:
            write_line(i, ' '.join([str(i) for i in xrange(1, K+1)]))
    else:
        if S < K - 1:
            write_line(i, 'IMPOSSIBLE')
        if K == 1:
            write_line(i, '1')
        else:
            write_line(i, ' '.join([str(i+1 + (i-1)*K*(C-1)) for i in xrange(1, K)]))

fi.close()
fo.close()