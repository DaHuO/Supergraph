from solver import solver

mapping = {
    'P': 'PR',
    'S': 'SP',
    'R': 'RS'}

def rec(s, n):
    if not n:
        return s
    return ''.join(sorted(rec(c, n-1) for c in mapping[s]))

def possible(n):
    a, b, c = 1, 0, 0
    for x in range(n):
        a, b, c = a + c,  b + a, c + b
    return a, b, c

@solver
def showdown(lines):
    n, r, p, s = map(int, lines[0].split())
    d = {(r, s, p): 'R',
         (s, p, r): 'S',
         (p, r, s): 'P'}
    key = possible(n)
    if key not in d:
        return 'IMPOSSIBLE'
    return rec(d[key], n)

if __name__ == '__main__':
    showdown.from_cli()
