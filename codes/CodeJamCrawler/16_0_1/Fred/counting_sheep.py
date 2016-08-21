from base import *

class CountingSheepSolver (CodeJamSolver):
    def read_instance(self, f):
        return int(f.readline())

    def solve_instance(self, n):
        if n == 0:
            return 'INSOMNIA'

        def get_digits(i):
            if i == 0:
                yield 0
            else:
                while i > 0 :
                    yield i % 10
                    i /= 10

        digits = set()

        for i in xrange(1, 10000000000): # FIXME : range
            for d in get_digits(n * i):
                digits.add(d)

            if len(digits) == 10:
                return str(n * i)

        if len(digits) < 10:
            return 'INSOMNIA'

if __name__ == '__main__':
    solver = CountingSheepSolver()
    solver.run()

    # print solver.solve_instance(1692*1692*1692)
