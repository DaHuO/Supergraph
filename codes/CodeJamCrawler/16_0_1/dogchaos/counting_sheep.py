

class Template:
    def process(self, fin, fout):
        numset = set()
        N = int(fin.readline().strip())
        ans = N
        if ans == 0:
            print 'INSOMNIA'
            fout.write('INSOMNIA')
            return
        while True:
            # print ans
            strN = str(ans)
            for i in strN:
                numset.add(i)
            if len(numset) == 10:
                break
            ans += N

        print str(ans)
        fout.write(str(ans))

    def solve(self):
        # fin = open('../boomerang_constellations.txt', 'r')
        # fin = open('../example.txt', 'r')
        fin = open('../in.in', 'r')
        fout = open('../out', 'w')
        times = int(fin.readline())
        for i in range(times):
            print 'Case #%d: ' % (i + 1)
            fout.write("Case #%d: " % (i + 1))
            self.process(fin, fout)
            fout.write("\n")
        fin.close()
        fout.close()

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('1\n2000\n')
        for i in range(2000):
            fout.write('%d %d\n' % ((-1000 + i), 1000 - i))
        fout.close()


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()
