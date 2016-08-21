
def g(x):
    if x == 0:
        return 'INSOMNIA'
    result = set()
    y = x;
    while result != set(range(0, 10)):
        result |= set(map(lambda x: int(x), str(x)))
        x += y
    return x-y

n = input()
for i in range(1, int(n)+1):
    x = input()
    print('Case #{}: {}'.format(i, g(int(x))))

