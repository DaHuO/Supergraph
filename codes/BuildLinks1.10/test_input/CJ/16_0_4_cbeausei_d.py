import sys

T = int(input())
for N in range(1, T + 1):
    out = 'Case #' + str(N) + ':'
    K, C, S = map(int, input().split())
    for i in range(K):
        out += ' ' + str(i + 1)
    out += '\n'
    sys.stdout.write(out)
    sys.stdout.flush()
    sys.stderr.write(out)
    sys.stderr.flush()