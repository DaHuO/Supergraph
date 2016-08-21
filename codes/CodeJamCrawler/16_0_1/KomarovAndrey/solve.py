
def last(n):
    if n == 0:
        return 'INSOMNIA'
    s = set()
    i = 0
    while len(s) < 10:
        i += 1
        s.update(str(i * n))
    return i * n

n = int(input())
for i in range(n):
    print('Case #{}: {}'.format(i + 1, last(int(input()))))
