import logging

logging.basicConfig(level=logging.INFO)

def digits(n):
    logging.debug('digits({})'.format(n))
    return [int(c) for c in str(n)]

def last(N):
    if not N:
        return 'INSOMNIA'
    seen = set()
    c = 1
    while True:
        n = c*N
        for d in digits(n):
            seen.add(d)
        if len(seen) == 10:
            return n
        c += 1

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        N = int(input())
        print('Case #{}: {}'.format(case + 1, last(N)))

