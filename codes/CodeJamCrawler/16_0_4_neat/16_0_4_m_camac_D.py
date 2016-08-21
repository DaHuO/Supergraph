T = input()

def solve(k, c, s):
    pos = [1 + i * pow(k, c - 1) for i in range(s)]
    return ' '.join(map(str, pos))

for i in range(1, T + 1):
    print 'Case #{}: {}'.format(i, solve(*map(int, raw_input().strip().split())))
