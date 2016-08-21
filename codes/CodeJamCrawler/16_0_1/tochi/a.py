def do(n):
    digits = [str(i) for i in range(10)]
    if n == 0:
        return 'INSOMNIA'
    for i in range(1, 1+1000):
        s = str(n * i)
        for d in digits.copy():
            if d in s:
                digits.remove(d)
        if len(digits) == 0:
            return s
    else:
        return 'INSOMNIA'

N = int(input())
for i in range(1, 1+N):
    n = int(input())
    print('Case #%d: %s' % (i, do(n)))
