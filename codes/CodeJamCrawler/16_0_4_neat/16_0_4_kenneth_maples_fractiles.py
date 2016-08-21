
def expand(a, v):
    s = ''
    for c in v:
        if c == 'L':
            s += a
        else:
            s += 'G' * len(a)
    return s

def all_words(n):
    if n == 1:
        return ['L', 'G']
    return ['L' + x for x in all_words(n-1)] + ['G' + x for x in all_words(n-1)]

def showall(examples, complexity):
    for ex in examples:
        v = ex
        for k in range(complexity):
            v = expand(ex, v)
        print v

def fractiles(k, c, s):
    
    if k % c == 0:
        needed = k/c
    else:
        needed = k/c + 1
    if s < needed:
        return 'IMPOSSIBLE'

    # need numbers base k that have all possible coefficients from 0 through k-1.
    # the maximum value is k^c - 1 which gives us c values per sample.
    values = []
    for t in range(needed):
        # t th example. each must represent c values.
        # 0 : 0, 1, .., c-1
        # 1 : c, c+1, .., 2c-1
        # 2: 2c, 2c+1, ...
        coefficients = range(t*c, (t+1)*c)
        coefficients = [x for x in coefficients if x < k] # exclude unneeded/bad elements
        # print coefficients
        value = sum([x * k**m for (m,x) in enumerate(coefficients)])
        # print value
        values += [value + 1]
    
    return values[:needed]

def main():
    t = int(raw_input().strip())
    for j in range(t):
        line = raw_input().strip()
        inputs = line.split()
        k, c, s = int(inputs[0]), int(inputs[1]), int(inputs[2])
        result = fractiles(k,c,s)
        if type(result) == list:
            result = ' '.join([str(t) for t in result])

        print 'Case #' + str(j+1) + ': ' + result

if __name__ == '__main__':
    main()

