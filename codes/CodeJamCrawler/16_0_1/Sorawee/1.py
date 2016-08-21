import sys

content = sys.stdin.read().split()[1:]
set_all = set(range(10))

def ans(v):
    seen = set()
    for i in range(1, 200):
        seen = seen | {int(c) for c in str(v * i)}
        if seen == set_all:
            return i * v
    return 'INSOMNIA'

for i, v in enumerate(content):
    print('Case #{}: {}'.format(i + 1, ans(int(v))))