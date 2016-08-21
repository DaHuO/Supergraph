import sys
lines = map(lambda x: x.strip(), sys.stdin.readlines())

vals = map(lambda x: int(x), lines[1:])
case = 0
for val in vals:
  case += 1
  if val == 0:
    print("Case #{0}: INSOMNIA".format(case))
  else:
    seen = [0] * 10
    n = 0
    while sum(seen) < 10:
      n += val
      for digit in str(n):
        seen[int(digit)] = 1
    print("Case #{0}: {1}".format(case, n))
