import re

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = long(input())  # read a line with a single longeger
for i in range(1, t + 1):
  cakes = str(raw_input())
  if(not '-' in cakes):
    o = 0
  else:
    group = re.findall('\-+',cakes)
    o = 2*len(group)
    if cakes[0] == '-':
      o = o - 1
  print("Case #{}: {}".format(i, o))
