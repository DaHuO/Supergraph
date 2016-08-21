input = open('./cl.in')
output = open('./cl.out', 'w')

T = int(input.readline())
N, J = [int(x) for x in input.readline().split(' ')]
output.write('Case #%d:\n' % (1))
def calc(s, base):
    ret = 0
    for x in s:
        ret *= base
        if(x == '1'):
            ret += 1
    return ret
for i in range(J):
    b = 2 ** (N / 2 - 1) + i * 2 + 1

    s = bin(b)[2:]
    output.write('%s' % (s + s))
    for j in range(2, 11):
        if(calc(s + s, j) % int(s, j) != 0):
            print 'not ok'
        output.write(' %d' % int(s, j))
    output.write('\n')