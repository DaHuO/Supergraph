def solve(n):
  steps = 0
  used = [False] * 10
  num_used = 0
  x = 0
  while num_used < 10:
    steps += 1
    x += n
    for char in str(x):
      digit = int(char)
      if not used[digit]:
        used[digit] = True
        num_used += 1
  return [x, steps]

with open('A-large.in') as f:
  lines = f.readlines()
  T = int(lines[0])
  for testcase in range(1, T + 1):
  	n = int(lines[testcase])
  	res = "INSOMNIA"
  	if n > 0:
  	  res = str(solve(n)[0])
  	print "Case #%d: %s" % (testcase, res)
