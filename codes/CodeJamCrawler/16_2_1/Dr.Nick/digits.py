#!/usr/bin/env python

import sys

#build discounts so its easy to substract them
digits = [ 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE' ]
d_global_counts = []
for i in digits:
  d = {}
  for char in i:
    if char not in d:
      d[char] = 0
    d[char]+=1
  d_global_counts.append(d)

cases = int(sys.stdin.readline().strip())

def find_number(num_str):
  d = {}
  d_total = 0
  for char in num_str:
    if char not in d:
      d[char] = 0
    d[char] += 1
    d_total += 1

  #try all posible ones
  actives = [ ([], d, d_total) ]
  while True:
    nums, d, d_total = actives.pop()

    for num in range(nums[-1] if len(nums) > 0 else 0, 10):
      new_d = d.copy()
      new_d_total = d_total
      wrong = False
      for char in d_global_counts[num]:
        if char in new_d and \
            new_d[char] >= d_global_counts[num][char]:
          new_d[char] -= d_global_counts[num][char]
          new_d_total -= d_global_counts[num][char]
        else:
          #abort this search if not possible
          wrong = True
          break
      if wrong:
        continue

      new_nums = nums + [num]

      if new_d_total == 0:
        return "".join([str(x) for x in new_nums])
      actives.append((new_nums, new_d, new_d_total))

for c in xrange(cases):
  line = sys.stdin.readline().strip()
  print "Case #%d: %s" %(c+1, find_number(line))

