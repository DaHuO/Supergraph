t = int(input())
for x in range(1, t + 1):
    n = int(input())
    last = n
    seen = set()
    if n:
        while seen != set('0123456789'):
            seen |= set(str(last))
            last += n
        last -= n
    else:
        last = 'INSOMNIA'
    print('Case #{}: {}'.format(x, last))
