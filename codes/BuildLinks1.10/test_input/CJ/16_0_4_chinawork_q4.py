__author__ = 'zfeng'

def solver(line):
    d = [int(i) for i in line.strip().split()]
    k, c, s = d[0], d[1], d[2]

    res = ''

    ivl = pow(k, c - 1)

    l = 1
    for i in xrange(k):
        res += str(l) + ' '
        l += ivl
    return res.strip()

if __name__ == '__main__':
    f = open('/Users/zfeng/Downloads/D-small-attempt0.in')
    lines = f.readlines()
    f.close()

    for i in xrange(int(lines[0])):
        print str.format('Case #{0}: {1}', i + 1, solver(lines[i + 1]))

