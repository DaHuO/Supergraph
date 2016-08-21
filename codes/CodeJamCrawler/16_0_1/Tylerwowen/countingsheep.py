import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    N = str.strip(sys.stdin.readline())
    if N == '0':
        print('Case #' + str(i) + ': INSOMNIA')
        continue
    checks = [False]*10
    done = False
    j = 1
    n = n_i = int(N)
    while not done:
        for c in N:
            checks[int(c)] = True
        done = checks[0]
        for check in checks:
            done = done and check
        if done:
            break
        n += n_i
        N = str(n)

    print('Case #' + str(i) + ': ' + N)
