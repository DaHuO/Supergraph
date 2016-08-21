import math
import itertools
from collections import Counter
from collections import deque

strings = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

# mapping = {
# 	0: 'ZERO',
# 	''
# }

first = ['ZERO', 'TWO', 'THREE', 'FOUR', 'SIX', 'EIGHT']


T = int(raw_input())

for case_no in xrange(1, T + 1):
    ans = []

    s = raw_input()
    counter = Counter(s)
    while sum(counter.values()):
    	while counter['Z']:
    		counter -= Counter('ZERO')
    		ans.append(0)
    	while counter['W']:
    		counter -= Counter('TWO')
    		ans.append(2)
    	while counter['U']:
    		counter -= Counter('FOUR')
    		ans.append(4)
    	while counter['X']:
    		counter -= Counter('SIX')
    		ans.append(6)
    	while counter['G']:
    		counter -= Counter('EIGHT')
    		ans.append(8)
    	while counter['H']:
    		counter -= Counter('THREE')
    		ans.append(3)
    	while counter['O']:
    		counter -= Counter('ONE')
    		ans.append(1)
    	while counter['F']:
    		counter -= Counter('FIVE')
    		ans.append(5)
    	while counter['S']:
    		counter -= Counter('SEVEN')
    		ans.append(7)
    	while counter['I']:
    		counter -= Counter('NINE')
    		ans.append(9)

    	ans.sort()

    	res = map(str, ans)
    	res = ''.join(res)

    print 'Case #{}: {}'.format(case_no, res)