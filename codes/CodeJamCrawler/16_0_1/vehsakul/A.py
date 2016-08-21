import fileinput

get = lambda t: list(t(i) for i in input.readline().strip().split())

def solve_case():
    N, = get(int)
    n = N
    digits = set(str(N))
    #print(digits)
    if N == 0:
        return 'INSOMNIA'
    else:
        while len(digits) != 10:
            N += n
            digits |= (set(str(N)))
        return N




with fileinput.input() as input:
    T, = get(int)
    for c in range(T):
        print('Case #%s: %s' % (c+1, solve_case()))


