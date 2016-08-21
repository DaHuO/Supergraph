import sys

def solve():
    T = int(io.readline()) + 1
    f = "Case #{0}: {1}";
    for t in range(1,T):
        a = 0
        N = io.readline()
        if N != '0':
            s = set([int(x) for x in N])
            N = int(N)
            r = N
            while len(s) < 10:
                r += N
                s.update([int(x) for x in str(r)])
            io.write(f.format(t, r))
        else:
            io.write(f.format(t, "INSOMNIA"))

class InOut:
    def __init__(self, inFile=True, outFile=True):
        self.fin = open('test.in', 'r') if inFile else sys.stdin
        self.fout = open('test.out', 'w') if outFile else sys.stdout
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.fin.close()
        self.fout.close()
    def write(self, *s, sep='', end='\n'):
        print(*s, sep=sep, end=end, file=self.fout)
    def readline(self):
        return self.fin.readline().rstrip()
    def read(self):
        return self.fin.read().rstrip()

with InOut() as io:
    solve()
