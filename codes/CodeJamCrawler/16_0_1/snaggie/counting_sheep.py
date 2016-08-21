#!/usr/bin/env python

def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'

    nums = set()
    for i in xrange(1, 1000001):
        shout = n*i
        nums.update(set(str(shout)))
        if len(nums) == 10:
            return shout
        elif len(nums) > 10:
            raise 'Problem...'
    return 'INSOMNIA'

# print count_sheep(2)

t = int(raw_input())
for i in xrange(1, t + 1):
  n = int(raw_input())
  print "Case #{}: {}".format(i, count_sheep(n))
