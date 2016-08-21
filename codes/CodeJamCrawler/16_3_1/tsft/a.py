from string import ascii_uppercase
from heapq import *
import itertools

def solve(senators, total):
  plan = []
  while total:
    soln = ''
    neg_count, party = heappop(senators)
    heappush(senators, (neg_count + 1, party))
    total -= 1
    soln += party
    count = (-senators[1][0])
    if count <= (total - 1)/2:
      neg_count, party = heappop(senators)
      heappush(senators, (neg_count + 1, party))
      soln += party
      total -= 1
    plan.append(soln)
  return plan


n = int(raw_input())
for case in range(1, n + 1):
  _ = int(raw_input())
  nums = map(int, raw_input().split())
  total = sum(nums)
  senators = [(-n, ascii_uppercase[i]) for i, n in enumerate(nums)]
  heapify(senators)
  result = solve(senators, total)
  print "Case #{0}: {1}".format(case, ' '.join(result))