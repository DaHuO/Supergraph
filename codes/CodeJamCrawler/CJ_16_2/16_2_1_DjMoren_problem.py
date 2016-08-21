'''
Created on Apr 16, 2016

@author: hduser
'''
from collections import OrderedDict


def solve_number(s, numbers):
    for number in numbers:
        n_list = list(number)
        enc = True
        scopy = s[:]
        for n in n_list:
            if n not in scopy:
                enc = False
                break
            else:
                scopy.remove(n)
        if enc:
            for n in list(number):
                s.remove(n)
            return numbers[number], s


def solve(s):
    numbers = OrderedDict()
    numbers['ZERO'] = 0
    numbers["TWO"] = 2
    numbers["SIX"] = 6
    numbers["EIGHT"] = 8
    numbers["THREE"] = 3
    numbers["FOUR"] = 4
    numbers["FIVE"] = 5
    numbers["SEVEN"] = 7
    numbers["ONE"] = 1
    numbers["NINE"] = 9
    s = list(s)
    sol = ''
    while len(s) > 0:
        n, s = solve_number(s, numbers)
        sol += str(n)
    else:
        return ''.join(sorted(sol))


t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, solve(s))
