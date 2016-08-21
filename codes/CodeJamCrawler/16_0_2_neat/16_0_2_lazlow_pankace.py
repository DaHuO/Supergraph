import re
import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
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


pattern_pos = re.compile(r'\++')
pattern_neg = re.compile(r'-+')

# matches = list(re.finditer(pattern_pos, inp))


def simplify(inp):
    inp = re.sub(pattern_pos, '+', inp)
    return re.sub(pattern_neg, '-', inp)

@memoized
def process_pancakes(inp_string):
    if inp_string.startswith('+') and inp_string.endswith('+'):
        return inp_string.count('+') + inp_string.count('-') - 1
    elif inp_string.startswith('-') and inp_string.endswith('-'):
        return inp_string.count('+') + inp_string.count('-')
    elif inp_string.startswith('-') and inp_string.endswith('+'):
        return inp_string.count('+') + inp_string.count('-') - 1
    elif inp_string.startswith('+') and inp_string.endswith('-'):
        return inp_string.count('+') + inp_string.count('-')


if __name__ == '__main__':
    num_cases = int(input())
    for i in range(1, num_cases + 1):
        print('Case #{}: {}'.format(i, process_pancakes(simplify(input()))))
