import sys

def solve():
    T = int(io.readline()) + 1
    f = "Case #{0}: {1}";
    for t in range(1,T):
        count = 0
        S = io.readline()
        i = 1
        current = S[0]
        while i < len(S):
            if S[i] != current:
                count += 1
                current = S[i]
            i += 1
        if current != '+':
            count += 1
        io.write(f.format(t, count))

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
