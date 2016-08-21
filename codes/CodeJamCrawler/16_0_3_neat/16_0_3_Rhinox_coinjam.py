# python 2.7

class Input:
    def __init__(self, fp): self.fp = fp
    def m(self, n, t=str):  return [map(t, list(self.line())) for i in range(n)]
    def ms(self, n, t=str, sep=' '):  return [map(t, self.line().split(sep)) for i in range(n)]
    def line(self):  return self.fp.readline().strip()
    def words(self): return self.line().split()
    def int(self):   return int(self.line())
    def ints(self):  return map(int, self.words())
    def float(self): return float(self.line())
    def floats(self):return map(float, self.words())
    def str(self):   return self.line()
    def types(self, *types): return [t(w) for t,w in zip(types, self.words())]

from itertools import islice, combinations, product
def take(n, iterable): return list(islice(iterable, n))

def setBitIndices(value, indices):
    for i in indices:
        value |= 1 << i
    return value

if __name__ == "__main__":
    import os, sys

    fn = "C-test.in" if len(sys.argv) <= 1 else sys.argv[1]
    f = Input(open(fn))
    fout = open(os.path.splitext(fn)[0] + ".out", "w")

    def answer(t, ans):
        o = "Case #%d: %s\n"%(t, ans)
        sys.stdout.write(o)
        fout.write(o)

    # Note: PoC. N has a lower bound here (and dependant of J)
    divisors = " ".join(str(x + 1) for x in range(2, 11))
    for case in range(f.int()):
        N, J = f.ints()
        base = (1 << (N - 1)) + 1

        nEvens, nOdds = (N/4,) * 2
        if N % 2 == 1:
            nEvens -= 2

        prod = product( combinations(range(2, N - 1, 2), nEvens),
                        combinations(range(1, N - 1, 2), nOdds))
        l = ["%s %s"%(bin(setBitIndices(base, a + b))[2:], divisors) for (a, b) in take(J, prod)]

        answer(case + 1, "\n" + "\n".join(l))

        if len(set(l)) != J:
            print "ERROR! Couldn't find enough numbers: %d"%((len(l) - 1))
