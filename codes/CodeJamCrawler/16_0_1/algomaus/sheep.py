#! /usr/bin/env python

def parse(lines):
  n = int(lines[0])
  numbers = []
  for i in range(n):
    line = lines[i+1]
    numbers.append(int(line))
  return numbers

def solve(num):
  if num == 0:
    return num
  missing = set(['1','2','3','4','5','6','7','8','9','0'])
  maxIt = 500000
  actIt = 0
  actnum = num
  while actIt < maxIt:
    actnumAsString = str(actnum)
    for i in actnumAsString:
      if i in missing:
        missing.remove(i)
    if len(missing) == 0:
      return actnum
    else:
      actnum = actnum + num
      actIt = actIt + 1
  return 0
    
with open('A-large.in', 'r') as f:
#with open('input', 'r') as f:
  numbers = parse(f.read().splitlines())
for i in range(len(numbers)):
  sol = solve(numbers[i])
  if sol > 0:
    print "Case #" + str(i+1) + ": " + str(sol)
  else:
    print "Case #" + str(i+1) + ": INSOMNIA"
