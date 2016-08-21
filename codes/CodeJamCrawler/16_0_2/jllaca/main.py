def flip(s, i):
    a = ''
    for j in range(i):
        a += '+' if s[i - j - 1] == '-' else '-'
    return a + s[i:]

def min_flips(s):
    if not s:
        return 0
    i = s.rfind('-')
    if i < 0:
        return 0
    if s[0] == '+':
        j = 1
        while j < len(s) and s[j] == '+':
            j += 1
        return 1 + min_flips(flip(s, j))
    return 1 + min_flips(flip(s, i + 1))

t = input()
for i in range(t):
    s = raw_input()
    n = min_flips(s)
    print 'Case #{}: {}'.format(i + 1, n)
