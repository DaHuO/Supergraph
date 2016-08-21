

class Template:
    def __init__(self):
        self.ans_dict = {}
        self.ans_dict[0] = 0
        for i in range(1, 101):
            if i % 2 == 1:
                self.ans_dict[i] = 1 + self.ans_dict[i - 1]
            else:
                self.ans_dict[i] = 2 + self.ans_dict[i - 2]

    def process(self, fin, fout):
        S = fin.readline().strip()
        print S
        data = [x for x in S]
        data = self.remove_duplicate(data)
        if data[-1] == '+':
            data = data[:len(data) - 1]
        ans = self.ans_dict[len(data)]

        print str(ans)
        fout.write(str(ans))

    def remove_tail_p(self, data):
        l = len(data)
        tail = l
        for i in reversed(range(l)):
            if data[i] == '-':
                break
            tail = i
        return data[:tail]

    def remove_duplicate(self, data):
        a = data[0]
        new_data = [a]
        data = data[1:]
        for b in data:
            if b != a:
                new_data.append(b)
                a = b
        return new_data

    def flip(self, data, num):
        new_data = ['-' if x == '+' else '+' for x in reversed(data)]
        return new_data

    def solve(self):
        fin = open('../in.in', 'r')
        # fin = open('../test', 'r')
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
