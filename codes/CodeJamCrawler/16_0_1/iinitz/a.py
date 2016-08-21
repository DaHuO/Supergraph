def counting(n):
    if n == 0:
        return 'INSOMNIA'
    ss = set('0123456789')
    s = set()
    i = 1
    m = n
    while True:
        s |= set(str(m))
        if s == ss:
            return str(m)
        else:
            i += 1
            m = n * i
for t in range(int(input())):
    print('Case #%d: %s'%(t+1, counting(int(input()))))
