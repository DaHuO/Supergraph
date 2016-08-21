import fileinput

get = lambda t: list(t(i) for i in input.readline().strip().split())

def solve_case():
    stack, = get(str)   
    stack = stack[::-1] 
    prev = stack[0]
    result = int(stack[0] == '-')
    for c in stack[1:]:
        if prev != c:
            result += 1
        prev = c
    return result

with fileinput.input() as input:
    T, = get(int)
    for c in range(T):
        print('Case #%s: %s' % (c+1, solve_case()))


