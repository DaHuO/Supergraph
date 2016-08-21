import sys
import pdb


def count_sheep(n):
    n = int(n)
    if n == 0:
        return 'INSOMNIA'
    match = set(map(str, range(10)))
    digits = set()
    n_culm = n

    while True:
        digits = digits | set(list(str(n_culm)))
        if digits == match:
            return str(n_culm)
        print "%d\r" % n_culm,
        n_culm += n
        # pdb.set_trace()


with open(sys.argv[1], 'r') as fp:
    inp = fp.readlines()

T = int(inp.pop(0))

with open(sys.argv[1] + '.out', 'w') as fp:
    for idx, line in enumerate(inp):
        case = int(line.strip())
        result = count_sheep(case)
        try:
            outp = 'Case #%d: %s' % (idx + 1, result)
        except TypeError:
            pdb.set_trace()
        print '\n' + outp
        fp.write(outp + '\n')
