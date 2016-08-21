from itertools import product

class CountingSheep:

    def __init__(self, input_name):
        self.input_name = input_name
        self.Ns = list()
        self.res = list()
        self.input()
        self.find_last_number()
        self.output()

    def input(self):
        with open(self.input_name + '.in', 'r') as f:
            for i, l in enumerate(f):
                l = l.split('\n')[0]
                if i >= 1:
                    self.Ns.append(int(l.split()[0]))

    def output(self):
        output_name = 'output_' + self.input_name + '.out'
        with open(output_name, 'w') as f:
            for i, r in enumerate(self.res):
                printline = 'Case #' + str(i + 1) + ': {0} \n'.format(str(r))
                print(printline)
                f.write(printline)

    def remove_digits(self, num):
        for digit in [int(e) for e in str(num)]:
            if digit in self.digits_not_seen:
                self.digits_not_seen.remove(digit)

    def find_last_number(self):
        for N in self.Ns:
            if N == 0:
                self.res.append('INSOMNIA')
            else:
                self.digits_not_seen = list(range(10))
                last_number = 0
                while self.digits_not_seen:
                    last_number += 1
                    self.remove_digits(last_number * N)
                self.res.append(last_number * N)

if __name__ == '__main__':
    w = CountingSheep('A-large')
