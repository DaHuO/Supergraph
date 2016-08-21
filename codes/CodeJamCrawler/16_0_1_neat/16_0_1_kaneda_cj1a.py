
inpunts = open('A-large.in').read().split('\n')
n_input = int(inpunts[0])
inpunts = inpunts[1:-1]


class Output(object):
    case = 1
    case_s = 'Case #'
    out_f = open('A-large.out', 'w')

    def __init__(self):
        super(Output, self).__init__()

    def add_case(self, n):
        s = 'Case #%d: %s' % (self.case, 'INSOMNIA' if n == 0 else str(n))
        if self.case != 1:
            s = '\n' + s
        self.out_f.write(s)

        self.case += 1

    def close(self):
        self.out_f.close()

output = Output()
for N in inpunts:
    N = int(N)
    if N == 0:
        output.add_case(N)
    else:
        digits = set([])
        i = 1
        while len(digits) != 10:
            digits |= set([int(c) for c in list(str(N*i))])
            i += 1
        output.add_case(N * (i-1))
output.close()
