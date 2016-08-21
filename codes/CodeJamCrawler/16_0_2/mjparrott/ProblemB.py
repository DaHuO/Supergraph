# Revenge of the Pancakes
import sys
f = open(sys.argv[1], "r")

n = int(f.readline())

def rindex(lst, item):
  for ind, x in enumerate(reversed(lst)):
    if x == item:
      return len(lst) - ind - 1

for case_num, case in enumerate(f):
  case = case.strip()
  expected = "+" * len(case)
  count = 0

  current = list(case)
  while ''.join(current) != expected:
    minus_pos = rindex(current, '-')
    for i in range(minus_pos + 1):
      if current[i] == '-':
        current[i] = '+'
      else:
        current[i] = '-'
    count += 1
  
  print("Case #{}: {}".format(case_num + 1, count))

f.close()
