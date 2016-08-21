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


@memoized
def order_digits_in_string(inp):
    return ''.join(sorted(set([i for i in inp])))


def see_numbers(inp):
    if inp == str(0):
        return 'INSOMNIA'

    digits = order_digits_in_string(inp)
    multiplier = 2
    while digits != '0123456789':
        last_num = str(multiplier * int(inp))
        digits = order_digits_in_string(digits + last_num)
        multiplier += 1

    return last_num


if __name__ == '__main__':
    num_cases = int(input())
    for i in range(1, num_cases + 1):
        print('Case #{}: {}'.format(i, see_numbers(input())))
