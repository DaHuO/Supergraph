import sys

def run(N):
    if not N: return 'INSOMNIA'
    touched = [0]*10
    c = 0
    while sum(touched) < 10:
        c += N
        for w in str(c):
            touched[int(w)] = 1
    return c

fin = file(sys.argv[1])
T = int(fin.readline().strip())
for i in range(1,T+1):
    N = int(fin.readline().strip())
    ans = run(N)
    print('Case #%d: %s' % (i, ans))
