import numpy as np
import math

class Case:
    def __init__(self):
        self.k = 0

    def solve(self):
        return ' '.join(map(str, range(1, self.k+1)))


def read_case(file):
    case = Case()
    line = file.readline().split(' ')
    line = map(int, line)
    case.k = line[0]
    return case


def main():
    filename_in = 'D-small-attempt0.in'
    filename_out = 'D-small-attempt0.out'
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