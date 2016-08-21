ifile = 'A-large.in'
ofile = 'output.txt'
input = open(ifile, 'r')
output = open(ofile, 'w')

digits = '1234567890'
def count_sheep(n):
    if n == 0:
        return -1
    j = 0
    s = set(i for i in digits)
    k = 0
    while s:
        j += n
        for x in str(j):
            s.discard(x)
    if s:
        return -1
    return j

i = int(input.readline())
for j in xrange(1, i+1):
    n = int(input.readline())
    ans = count_sheep(n)
    st = ''
    if ans == -1:
        st = 'Case #%d: INSOMNIA\n' % j
    else:
        st = 'Case #%d: %d\n' % (j, ans)
    output.write(st)