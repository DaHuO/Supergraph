
import fileinput

get = lambda t: list(t(i) for i in input.readline().strip().split())

def solve_case():
    K, C, S = get(int)
    return ' '.join(str(i+1) for i in range(K)) 


with fileinput.input() as input:
    T, = get(int)
    for c in range(T):
        print('Case #%s: %s' % (c+1, solve_case()))


