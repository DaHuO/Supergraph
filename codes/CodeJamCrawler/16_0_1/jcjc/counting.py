import sys

f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    seen = [False]*10
    N = int(f.readline())
    i = 1
    result = N
    if N == 0:
        result = 'INSOMNIA'
    else:
        while not all(seen):
            for digit in str(i*N):
                seen[int(digit)] = True
            i = i + 1
        result = N*(i-1)
    print 'Case #{}: {}'.format(t+1, result)
