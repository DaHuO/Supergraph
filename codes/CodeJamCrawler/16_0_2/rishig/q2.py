import sys, re

def run(N):
    cnt = 0
    for i in range(len(N)-1):
        cnt += int(N[i] == '+' and N[i+1] == '-')
    return 2*cnt + int(N[0] == '-')

fin = file(sys.argv[1])
T = int(fin.readline().strip())
for i in range(1,T+1):
    N = fin.readline().strip()
    ans = run(N)
    print('Case #%d: %s' % (i, ans))
