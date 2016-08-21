import numpy as np
import math

class Case:
    def __init__(self):
        self.letters = {
            'Z': 0,
            'E': 0,
            'R': 0,
            'O': 0,
            'N': 0,
            'T': 0,
            'W': 0,
            'H': 0,
            'F': 0,
            'U': 0,
            'I': 0,
            'V': 0,
            'S': 0,
            'X': 0,
            'G': 0,
        }

        self.digits = []

    def add(self, letter):
        if letter in self.letters:
            self.letters[letter] += 1

    def remove(self, s):
        for c in s:
            self.letters[c] -= 1

    def solve(self):
        # ZERO
        for i in range(self.letters['Z']):
            self.digits.append(0)
            self.remove('ZERO')

        # TWO
        for i in range(self.letters['W']):
            self.digits.append(2)
            self.remove('TWO')

        # FOUR
        for i in range(self.letters['U']):
            self.digits.append(4)
            self.remove('FOUR')

        # ONE
        for i in range(self.letters['O']):
            self.digits.append(1)
            self.remove('ONE')

        # THREE
        for i in range(self.letters['R']):
            self.digits.append(3)
            self.remove('THREE')

        # FIVE
        for i in range(self.letters['F']):
            self.digits.append(5)
            self.remove('FIVE')

        # SIX
        for i in range(self.letters['X']):
            self.digits.append(6)
            self.remove('SIX')

        # SEVEN
        for i in range(self.letters['S']):
            self.digits.append(7)
            self.remove('SEVEN')

        # EIGHT
        for i in range(self.letters['G']):
            self.digits.append(8)
            self.remove('EIGHT')

        # NINE
        for i in range(self.letters['I']):
            self.digits.append(9)
            self.remove('NINE')

        print self.letters

        self.digits.sort()

        return ''.join(map(str,self.digits))


def read_case(file):
    case = Case()
    line = file.readline()
    for l in line:
        case.add(l)
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