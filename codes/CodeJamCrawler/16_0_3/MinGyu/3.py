#!/usr/bin/env python

import random
import string
T = input()
N, J = map(int, raw_input().split(' '))
odd = range(1, N-2, 2)
even = range(0, N-2, 2)
print 'Case #1:'
cache = set()
result = []
for i in xrange(J):

    def get_num():
        while True:
            odd_pos = random.sample(odd,2)
            even_pos = random.sample(even,2)
            s = ['0']*(N-2)
            s[odd_pos[0]] = s[odd_pos[1]] = '1'
            s[even_pos[0]] = s[even_pos[1]] = '1'
            t_s = tuple(s)
            if t_s not in cache:
                cache.add(t_s)
                return s

    result.append('1{}1 3 2 5 2 7 2 3 2 11'.format(reduce(lambda a, b: a+b, get_num())))

result.sort()
print string.join(result,'\n')
