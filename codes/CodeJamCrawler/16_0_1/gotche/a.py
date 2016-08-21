import sys


class Prob1(object):
    def __init__(self, N):
        self.N = N

    def solve(self):

        n, i = self.N, 1
        digits = set()
        digits.update(list(str(n)))
        while i < 100:
            if len(digits) == 10:
                return str(n)
            i += 1
            n = self.N * i
            digits.update(list(str(n)))

        return 'INSOMNIA'


output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        N = int(f.readline())
        p1 = Prob1(N)
        print output % (counter+1, p1.solve())
