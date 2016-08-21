import sys
def run(f, infile_name):
    outfile_name = infile_name+'.out'
    with open(outfile_name, 'w') as outfile:
        for i, line in enumerate(open(infile_name)):
            line = line.rstrip()
            if i == 0:
                continue
            outfile.write('Case #{}: {}\n'.format(i, f(line)))

def counting_sheep(line):
    n = int(line)

    if n == 0:
        return 'INSOMNIA'

    x = n
    seen_digits = set()
    while len(seen_digits) < 10:
        seen_digits.update(set(str(x)))
        x += n

    return x-n

def revenge_of_pancakes(line):
    # continous + or - can be merged
    # trailing + can be drop
    # the rest is easy
    import numpy as np
    cakes = list(line)
    cakes_ = []
    prev_cake = None
    for c in cakes:
        if c != prev_cake:
            cakes_.append(c)
            prev_cake = c
    return len(cakes_) -1 if cakes_[-1] == '+' else len(cakes_)

def fractiles(line):
    # when C=2, n=a*K+b, S^2_n=0<=>S^1_a=0\/S^1_b=0
    from math import ceil
    k, c, s = list(map(int, line.split()))
    s_min = ceil(k/c)
    if s < s_min:
        return 'IMPOSSIBLE'
    solution = []
    pending = list(range(k))
    while pending:
        h, pending = pending[:c], pending[c:]
        x = 0
        for t in h:
            x = x*k+t
        solution.append(x+1)
    return ' '.join(map(str, solution))

if __name__ == '__main__':
    method_name = sys.argv[1]
    method = locals()[method_name]
    infile_name = sys.argv[2]
    run(method, infile_name)
