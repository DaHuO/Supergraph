def is_prime(n):
    if n < 3:
        return 0
    if n % 2 == 0:
        return 2
    for i in xrange(3, 31, 2):
        if i * i > n:
            break
        if n % i == 0:
            return i
    return 0

def dfs(n):
    if len(n) == 31:
        n += '1'
        m = [int(n, i + 2) for i in range(9)]
        m = map(is_prime, m)
        if 0 not in m:
            print n, ' '.join(map(str, m))
    else:
        dfs(n + '0')
        dfs(n + '1')

dfs('1')
