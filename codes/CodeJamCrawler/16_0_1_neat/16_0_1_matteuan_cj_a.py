def check(a):
    for i in a:
        if i == False:
            return False
    return True

def solve(N):
    if N == 0:
        return 'INSOMNIA'
    a = [False for i in range(10)]
    for i in range(1, 300):
        sn = str(N*i)
        for c in sn:
            a[int(c)] = True
        if check(a):
            return str(N * i)
    return 'INSOMNIA'


nf = input()
out = nf + ".out"
fout = open(out, 'w')
f = open(nf)
T = int(f.readline())
count = 1
for line in f:
    N = int(line)
    fout.write('Case #{}: {}\n'.format(count, solve(N)))
    count += 1
fout.close()
f.close()
