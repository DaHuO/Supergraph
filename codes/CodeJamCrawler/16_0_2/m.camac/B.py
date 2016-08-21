T = input()

def flip(s):
    return ''.join('+' if c == '-' else '-' for c in s)

def solve(s):
    moves = 0
    while '-' in s:
        pos = s.rfind('-')
        s = flip(s[:pos + 1]) + s[pos + 1:]
        moves += 1
    return moves

for i in range(1, T + 1):
    print 'Case #{}: {}'.format(i, solve(raw_input().strip()))
