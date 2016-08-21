fname = "A-large.in.txt"
# fname = "test.in"

def solve(n):
  if n == 0:
    return "INSOMNIA"

  digits = {int(i) for i in str(n)}
  new = n
  while len(digits) != 10:
    new += n
    digits = digits | {int(i) for i in str(new)}
  return new

def main():
  with open(fname) as f:
    for i in xrange(int(f.readline())):
      n = int(f.readline())
      print 'Case #%s: %s' % (i + 1, solve(n))

main()