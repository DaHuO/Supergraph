#!/usr/bin/python
from sets import Set

def read_file():
    f = open('A-large.in', 'r')
    return f.read().splitlines()


def calculate(line):
    sheep = Sheep(int(line))
    return sheep.find_last()


class Sheep():
    def __init__(self, start):
        self.start = start
        self.current = start
        self.multi = 1
        self.n_set = Set(str(start))

    def next(self):
        self.multi += 1
        next_num = self.start * self.multi

        self.current = next_num

        next_set = Set(str(next_num))
        self.n_set.update(next_set)

    def find_last(self):
        if self.start == 0:
            return 'INSOMNIA'

        while not self.check():
            self.next()

        return self.current

    def check(self):
        if len(self.n_set) == 10:
            return True
        return False



lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(1, t + 1):
    result = calculate(lines[i])
    print "Case #{}: {}".format(i, result)
