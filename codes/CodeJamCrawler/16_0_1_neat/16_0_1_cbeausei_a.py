import sys

def digits(n):
    if n < 10:
        return([n])
    l = digits(n // 10)
    l.append(n % 10)
    return(l)
    
K = 100
delta = 10000

T = int(input())
for N in range(1, T + 1):
    out = 'Case #' + str(N) + ': '
    n = int(input())
    asleep = False
    left = {}
    for i in range(10):
        left[i] = True
    k = 0
    while left != {} and k < K * (n + delta):
        k += 1
        dig = digits(k * n)
        for d in dig:
            if d in left:
                del left[d]
    if k < K * (n + delta):
        out += str(k * n)
    else:
        out += 'INSOMNIA'
    out += '\n'
    sys.stdout.write(out)
    sys.stdout.flush()
    sys.stderr.write(out)
    sys.stderr.flush()