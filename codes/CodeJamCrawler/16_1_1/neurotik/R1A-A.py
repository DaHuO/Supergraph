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

filename = 'A-large'
fi = file(filename + '.in', 'rb')
fo = file(filename + '.out', 'wb')



T = read_int()
for i in xrange(T):
    S = read_str()
    lastword = S[0]
    for c in S[1:]:
        if c < lastword[0]:
            lastword = lastword + c
        else:
            lastword = c + lastword

    write_line(i, lastword)




fi.close()
fo.close()