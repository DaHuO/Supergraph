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

if __name__ == "__main__":
    import os, sys

    fn = "D-test.in" if len(sys.argv) <= 1 else sys.argv[1]
    f = Input(open(fn))
    fout = open(os.path.splitext(fn)[0] + ".out", "w")

    def answer(t, ans):
        o = "Case #%d: %s\n"%(t, ans)
        sys.stdout.write(o)
        fout.write(o)

    for case in range(f.int()):
        size, exp, S = f.ints()

        #print size, exp, S
        slots = []
        for i in range(size):
            t = i
            for j in range(exp - 1):
                t = t * size + i
            slots.append(t)
        answer(case + 1, " ".join(str(x + 1) for x in slots))
