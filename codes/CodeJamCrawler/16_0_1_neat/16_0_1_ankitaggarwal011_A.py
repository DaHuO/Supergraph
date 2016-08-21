def solve(n):
  if n == 0:
    return "INSOMNIA"
  digits = set()
  i = 1
  while len(digits) < 10:
    d = getDigits(n * i)
    for digit in d:
      digits.add(digit)
    i += 1
  return n * (i - 1)

def getDigits(n):
  digits = []
  for d in str(n):
    digits.append(int(d))
  return digits

T = input ()
for t in xrange (1, T + 1):
  N = input ()
  print("Case #%i: %s" % (t, solve(N)))