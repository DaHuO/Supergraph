t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()  # read a list of integers, 2 in this case
  last = ""
  for l in s:
    if (len(last)):
      if (last[0] > l):
        last = last + l
      else:
        last = l + last
    else:
      last = l
  case_str = "Case #%d: " %i
  print case_str + last
