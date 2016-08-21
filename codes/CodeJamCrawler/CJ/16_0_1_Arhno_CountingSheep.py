import numpy as np
import math

class Case:
    def __init__(self):
        self.number = 0
        self._digit = [False] * 10

    def solve(self):
        if self.number == 0:
            return 'INSOMNIA'

        k = self.number
        self.update_digit(k)
        while False in self._digit:
            k += self.number
            self.update_digit(k)

        return str(k)

    def update_digit(self, n):
        while n > 0:
            n, d = divmod(n, 10)
            self._digit[d] = True



def read_case(file):
    case = Case()
    line = file.readline().split(' ')
    line = map(int, line)
    case.number = line[0]
    return case


def main():
    filename_in = 'A-large.in'
    filename_out = 'A-large.out'
    file_in = open(filename_in)
    file_out = open(filename_out, 'w')

    nb_case = int(file_in.readline())

    for k in range(1, nb_case + 1):
        case = read_case(file_in)
        to_write = 'Case #' + str(k) + ': ' + case.solve()
        print to_write
        file_out.write(to_write + '\n')

    file_out.close()


if __name__ == '__main__':
    main()