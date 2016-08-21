SHEEP = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def solve(N):
    if N == 0:
        return 'INSOMNIA'

    known = []
    i = 0
    n = N

    while True:
        s = str(n)
        for c in s:
            if c not in known:
                known.append(c)

        if SHEEP == sorted(known):
            return n

        i = i + 1
        n = i * N


if __name__ == '__main__':
    T = int(input())
    for t,i in enumerate(range(T)):
        N = int(input())
        print('Case #{0}: {1}'.format(i+1, solve(N)))
