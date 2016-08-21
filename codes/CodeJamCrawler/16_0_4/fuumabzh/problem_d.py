
class Fractiles:

    def __init__(self, input_name):
        self.input_name = input_name
        self.K = list()
        self.C = list()
        self.S = list()
        self.res = list()
        self.input()
        self.find_good_tiles()
        self.output()

    def input(self):
        with open(self.input_name + '.in', 'r') as f:
            for i, l in enumerate(f):
                l = l.split('\n')[0]
                if i >= 1:
                    K, C, S = [int(e) for e in l.split()]
                    self.K.append(K)
                    self.C.append(C)
                    self.S.append(S)

    def output(self):
        output_name = 'output_' + self.input_name + '.out'
        with open(output_name, 'w') as f:
            for i, r in enumerate(self.res):
                if r == []:
                    printline = 'IMPOSSIBLE'
                else:
                    printline = ' '.join([str(tile) for tile in r])
                printline = 'Case #' + str(i + 1) + ': {0} \n'.format(printline)
                print(printline)
                f.write(printline)

    def get_basic_answer(self, K, C, S):
        sum_K = 0
        for i in range(C):
            sum_K += K**i
        res = list()
        for i in range(K):
            res.append(i * sum_K + 1)
        return res

    def find_good_tiles(self):
        for K, C, S in zip(self.K, self.C, self.S):
            if self.test_impossible(K, C, S):
                self.res.append([])
            else:
                self.res.append(self.get_basic_answer(K, C, S))

    def test_impossible(self, K, C, S):
        return S < K


if __name__ == '__main__':
    w = Fractiles('D-small-attempt0')
