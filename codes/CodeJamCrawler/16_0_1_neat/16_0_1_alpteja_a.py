__author__ = 'prasannateja.aleti'
__email__ = 'alpteja@gmail.com'

import sys
import itertools
from collections import OrderedDict

class memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


def precalculate():
    pass


def read_input(infile):
    case = [int(i) for i in infile.readline().split()]
    return case


def solve_case(case):
    if case[0] == 0:
        return 'INSOMNIA'
    else:
        store=""
        store_default="0123456789"
        last_num=1
        iter=1

        while(store!=store_default):
            last_num=case[0]*iter
            # print last_num
            store="".join( "".join(sorted("".join(OrderedDict.fromkeys(store+str(last_num))))))
            iter+=1
            # print store
        # print last_num
        output=last_num
    return output


if __name__ == "__main__":
    assert len(sys.argv) == 2  # only one argument
    assert sys.argv[1][-3:] == ".in"  # input must end with .in
    infile = open("%s" % sys.argv[1], 'r')
    outfile = open("%s.out" % sys.argv[1][:-3], 'w')
    # infile = open("a.in", 'r')
    # outfile = open("a.out", 'w')

    cases = int(infile.readline().strip('\n'))
    for i in range(cases):
        case = read_input(infile)
        output = solve_case(case)
        outfile.write('Case #%i: %s\n' % (i + 1, output))
        print 'Case #%i: %s' % (i + 1, output)
    infile.close()
    outfile.close()
