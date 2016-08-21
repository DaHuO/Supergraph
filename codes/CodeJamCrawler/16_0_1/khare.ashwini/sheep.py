T = int(raw_input())
upper_limit = 10000
def getDigits(n):
    return [int(_) for _ in str(n)]

def process(N):
    if N == 0:
        return 'INSOMNIA'
    unmapped = range(0,10)
    multiplier = 2
    p = N
    iter = 0
    while True:
        g = getDigits(p)
        for digit in g:
            if digit in unmapped:
                unmapped.remove(digit)
        if len(unmapped) == 0:
            return p
        else:
            p = N * multiplier
            multiplier += 1
        iter += 1
        if iter > upper_limit:
            return 'INSOMNIA'
    

for i in range(1, T+1):
    N = int(raw_input())
    print('Case #{}: {}'.format(i, process(N)))
