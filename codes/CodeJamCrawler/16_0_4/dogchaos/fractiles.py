

class Template:
    def process(self, fin, fout):
        ans_list = []
        K, C, S = [int(x) for x in fin.readline().strip().split()]
        if C * S < K:
            print 'IMPOSSIBLE'
            fout.write('IMPOSSIBLE')
            return

        todo = range(K)
        while len(todo) > 0:
            todo_len = len(todo)
            if len >= C:
                dodo = todo[0:C]
                todo = todo[C:]
            else:
                dodo = [0 for _ in range(C - todo_len)] + todo
                todo = []
            ans_list.append(str(self.cal_loc(dodo, K, C)))

        ans = ' '.join(ans_list)
        print str(ans)
        fout.write(ans)

    def cal_loc(self, num_list, K, C):
        step = 1
        loc = 0
        for i in num_list:
            loc += i * step
            step *= K
        return loc + 1

    def solve(self):
        # fin = open('../boomerang_constellations.txt', 'r')
        fin = open('../in.in', 'r')
        # fin = open('../example.txt', 'r')
        fout = open('../out', 'w')
        times = int(fin.readline())
        for i in range(times):
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
