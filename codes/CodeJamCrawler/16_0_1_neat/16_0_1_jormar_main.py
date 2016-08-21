def hasSeenAll(seen):
  for key, value in seen.iteritems():
    if value == 0:
      return False

  return True


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for icase in xrange(1, t + 1):
  n, = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  result = "INSOMNIA"

  # print "   - Starting Case # {}".format(icase)

  seen = {}
  for x in xrange(0,10):
    seen[str(x)] = 0

  i=1
  lastValue = -1
  while True:
    value = i*n
    if lastValue==value:
      break

    for x in str(value):
      seen[x] = 1

    # print "   - Testing for {}".format(value)

    if hasSeenAll(seen):
      result = value
      break

    lastValue = value
    i = i+1


  print "Case #{}: {}".format(icase, result)
  # check out .format's specification for more formatting options

