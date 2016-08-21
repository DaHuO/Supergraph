def solve(line):
  if not line:
    return 0
  n = len(line) - 1
  if line[n] == '+':
    result = 0
  else:
    result = 1
  for i in xrange(n, 0, -1):
    if line[i] != line[i-1]:
      result += 1
  return result


tests = int(raw_input(''))

for i in xrange(1, tests + 1):
  line = raw_input('')
  print 'Case #%d: %d' % (i, solve(line))
