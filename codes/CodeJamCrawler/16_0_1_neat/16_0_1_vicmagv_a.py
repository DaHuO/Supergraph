fi = open('A-large.in', 'r')
fo = open('a-large.out', 'w')
size = fi.readline()

for case, line in enumerate(fi, start=1):
    fo.write('Case #{}: '.format(case))
    N_base = int(line.strip())
    N = N_base
    if N == 0:
        print('INSOMNIA')
        fo.write('INSOMNIA\n')
        continue
    digits = set()
    digits = digits | set(str(N))
    n = 2
    while len(digits) < 10:
        N = N_base*n
        digits = digits | set(str(N))
        n += 1
    print(N)
    fo.write(str(N)+'\n')
