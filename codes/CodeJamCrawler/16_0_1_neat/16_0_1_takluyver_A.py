import itertools

PROBLEM = 'A-large'

fin = open(PROBLEM+'.in', 'r')
fout = open(PROBLEM+'.out', 'w')

def read_ints():
    l = fin.readline().strip()
    return [int(x) for x in l.split()]

T, = read_ints()

def count_multiples(n):
    digits = set()
    for num in itertools.count(start=n, step=n):
        digits.update(str(num))
        if len(digits) == 10:
            return num


for caseno in range(1, T+1):
    print('Case #{}'.format(caseno))
    N, = read_ints()
    print('N =', N)
    if N == 0:
        res = 'INSOMNIA'
    else:
        res = count_multiples(N)
    print('res =', res)
    fout.write('Case #{}: {}\n'.format(caseno, res))
    print()
