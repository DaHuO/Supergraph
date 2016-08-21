
from itertools import groupby
from itertools import chain

HAPPY, BLANK = '+', '-'

class Pancake():
    def __init__(self, line):
        self.pancakes = self.merge_and_convert_bool(list(line))

    def merge_and_convert_bool(self, items):
        arr = self.merge_item(items)
        return arr

    def merge_item(self, items):
        shallow_list = [list(set(j)) for i, j in groupby(items)]
        arr = chain.from_iterable(shallow_list)
        return list(arr)

    def number_of_flip(self):
        if self.pancakes[-1] == HAPPY:
            return len(self.pancakes) - 1
        else:
            return len(self.pancakes)


def read_file():
    f = open('B-large.in', 'r')
    return f.read().splitlines()

lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(1, t + 1):
    pancake = Pancake(lines[i])
    print "Case #{}: {}".format(i, pancake.number_of_flip())
