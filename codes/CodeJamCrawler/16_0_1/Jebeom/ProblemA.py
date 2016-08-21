# Google Code Jam 2016
# Problem A
# by Jebeom Gyeong
# Twitter @JebeomGyeong

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import sys
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  n = int(raw_input())
  # n = i
  m = 1
  result = {}
  last_number = 0
  prev_name = ''

  while True:
    name = str(m * n)
    for c in name:
      result[c] = True

    digit_count = len(result)
    if digit_count == 10:
      last_number = name
      break

    if prev_name == name or m == sys.maxsize:
      last_number = "INSOMNIA"
      break

    prev_name = name

    m += 1

  print "Case #{}: {}".format(i, last_number)