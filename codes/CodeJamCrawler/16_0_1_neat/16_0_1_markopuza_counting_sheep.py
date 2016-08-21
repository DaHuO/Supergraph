for i in range(1, int(input()) + 1):
    digs = set()
    n = int(input())
    res = ''
    if n == 0:
        res = 'INSOMNIA'
    else:
        digs = set(str(n))
        cnt = 0
        j = 1
        while digs != set('0123456789'):
            j += 1
            digs = digs.union(set(str(j*n)))
        res = str(j*n)
    print('Case #'+ str(i) +': ' + res)
