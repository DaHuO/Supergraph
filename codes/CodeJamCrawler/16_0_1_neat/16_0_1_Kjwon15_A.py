def get_answer():
    n = int(input())
    s = set()
    for i in range(1, 100):
        num = n * i
        s.update(str(num))
        if len(s) == 10:
            return num
    else:
        return 'INSOMNIA'


n = int(input())

for t in range(1, n+1):
    print('Case #{}: {}'.format(t, get_answer()))
