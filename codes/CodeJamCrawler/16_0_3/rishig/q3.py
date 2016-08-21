import sys

class Counter:
    def __init__(self, N):
        self.c = [0]*N
        self.N = N

    def __next__(self):
        return self.nxt()

    def nxt(self):
        moo = 0
        while moo <= 2**N:
            moo += 1
            yield self.c
            for i in range(self.N):
                if self.c[i] == 0:
                    self.c[i] = 1
                    break
                else:
                    self.c[i] = 0

class Moo:
    def __init__(self):
        self.x = 0
    def nxt(self):
        yield self.x
        self.x += 1

fin = file(sys.argv[1])
T = int(fin.readline().strip())
for i in range(1,T+1):
    N,J = [int(x) for x in fin.readline().strip().split()]
    print('Case #1:')
    cnt = Counter((N-4) // 2)
    cc = cnt.nxt()
    for xxx in range(J):
        c = cc.next()
        print '100' + ''.join([str(blah)*2 for blah in c]) + '1' + ' 3 4 5 6 7 8 9 10 11'
