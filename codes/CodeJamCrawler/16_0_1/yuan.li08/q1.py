
def solve(n):
    if n == 0:
        return 'INSOMNIA'
    y = set(str(n))
    k = 1
    while len(y) != 10:
        k += 1
        y.update(set(str(n*k)))
    return str(n*k)

fname = 'test.txt'
fname = 'A-small-attempt0.in'
fname = 'A-large.in'
fin = open(fname)
lines = fin.readlines()
fin.close()

for k, line in enumerate(lines[1:]):
    print('Case #%d: ' % (k+1) + solve(int(line.strip())))
