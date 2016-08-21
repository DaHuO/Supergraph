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


chars = ['ZERO', 'TWO', 'FOUR', 'SIX', 'EIGHT', 'ONE', 'THREE',  'FIVE',  'SEVEN',  'NINE']
#           z      w      u       x       g        o      h        f         v         i
digits = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

d1 = '02468'
def get_nums(s):
    nums = []
    o = 0
    h = 0
    f = 0
    v = 0
    i = 0

    for j in xrange(s.count('Z')):
        o += 1
        nums.append('0')
    for j in xrange(s.count('W')):
        o += 1
        nums.append('2')
    for j in xrange(s.count('U')):
        o += 1
        f += 1
        nums.append('4')
    for j in xrange(s.count('X')):
        i += 1
        nums.append('6')
    for j in xrange(s.count('G')):
        i += 1
        h += 1
        nums.append('8')
    for j in xrange(s.count('O') - o):
        nums.append('1')
    for j in xrange(s.count('H') - h):
        nums.append('3')
    for j in xrange(s.count('F') - f):
        i += 1
        v += 1
        nums.append('5')
    for j in xrange(s.count('V') - v):
        nums.append('7')
    for j in xrange(s.count('I') - i):
        nums.append('9')

    return nums


T = read_int()
for i in xrange(T):
    write_line(i, ''.join(sorted(get_nums(fi.readline()))))


fi.close()
fo.close()