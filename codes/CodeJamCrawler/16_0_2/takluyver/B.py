PROBLEM = 'B-large'

fin = open(PROBLEM+'.in', 'r')
fout = open(PROBLEM+'.out', 'w')

def read_ints():
    l = fin.readline().strip()
    return [int(x) for x in l.split()]

T, = read_ints()

def min_flips(stack):
    stack += '+'
    n_changes = 0
    prev = stack[0]
    for p in stack[1:]:
        if p != prev:
            n_changes += 1
            prev = p
    return n_changes

for caseno in range(1, T+1):
    print('Case #{}'.format(caseno))
    stack = fin.readline().strip()
    print(stack)

    res = min_flips(stack)

    print('res =', res)
    fout.write('Case #{}: {}\n'.format(caseno, res))
    print()
