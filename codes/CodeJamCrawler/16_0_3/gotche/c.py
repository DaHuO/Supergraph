import sys
import math


def first_factor(number):
    for i in xrange(3, min(int(math.sqrt(number)) + 1, 100000), 2):
        if number % i == 0:
            return i
    else:
        return 0


class Prob1(object):
    def __init__(self, N, J):
        self.N = N
        self.J = J

    def solve(self):
        solutions = 0
        data = []
        first = ['0'] * self.N
        first[0] = first[self.N - 1] = '1'

        first = ''.join(first)
        last = ''.join(['1']*self.N)

#        print first
#        print last

        possibilities = 2**(self.N-2)
#        print "posibilities:", possibilities

        for counter in xrange(possibilities):
            candidate = int(first, 2) + 2*counter
            candidate = ''.join(list(bin(candidate))[2:])
#            print "-------------------", counter, candidate
            results = [candidate]
            for i in xrange(2, 11):
                digits = int(candidate, i)
                results.append(first_factor(digits))
#                print digits,
            #print results
#            print
            if 0 not in results:
                data.append(' '.join([str(j) for j in results]))
                solutions += 1

            if solutions == self.J:
                break
        return '\n'+'\n'.join(data)

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        N, J = [int(i) for i in f.readline().split()]
        p1 = Prob1(N, J)
        print output % (counter+1, p1.solve())
