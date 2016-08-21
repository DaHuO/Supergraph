# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
  str = list(raw_input())  # read a list of integers, 2 in this case
  new_str = ""
  for i, val in enumerate(str):
      if i == 0:
          new_str = val
      if len(str) != i + 1:
          if str[i + 1] < new_str[0]:
              new_str = new_str + str[i + 1]
          else:
              new_str = str[i + 1] + new_str
  print "Case #{}: {}".format(j, new_str)
  # check out .format's specification for more formatting options
