import numpy as np

def solve(line):
  n = int(line)
  seen = [0 for i in range(10)]
  nums = {}
  i = 1
  while not np.all(seen):
    num = n*i
    if num in nums:
      print "INSOMNIA"
      return
    nums[num] = 1
    for s in str(num): seen[int(s)] = 1
    i += 1

  print n*(i-1)



case = 1
with open('a.in') as f:
  next(f)
  for line in f:
    print "Case #"+str(case)+":",
    solve(line)
    case += 1
