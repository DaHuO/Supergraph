import itertools, math

def find_factor(n):
    if n % 2 == 0: return 2

    ceil = math.ceil(math.sqrt(n))
    for d in range(3, ceil + 1, 2):
        if n % d == 0: return d
    return n

def generate(N, J):
    ret = {}

    itrbl = filter(lambda x: x[0] == x[-1] == '1', map(lambda x: ''.join(x), itertools.product('01', repeat=N)))

    counter = 0
    while counter < J:
        x = next(itrbl)

        fs = []
        for base in range(2, 10 + 1):
            n = int(x, base)
            f = find_factor(n)
            if f != n:
                fs.append(f)
            else:
                break

        if len(fs) == 9:
            ret[x] = fs
            counter += 1

    return ret

if __name__ == '__main__':
    import sys, re

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        lines = f.read().strip().split('\n')

    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        N, J = map(int, re.split(' ', lines[0]))
        lines = lines[1:]

        d = generate(N, J)
        print('Case #{}:'.format(i))
        for k, v in d.items():
            print('{} {}'.format(k, ' '.join(map(str, v))))
