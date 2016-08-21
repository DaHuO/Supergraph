

def solve(n):
  if n == 0:
    return "INSOMNIA"
  
  s = set([ d for d in str(n) ])
  l = n
  while len(s) < 10:
    l += n
    s.update([ d for d in str(l) ])
  return str(l)

if __name__ == "__main__":
  t = int(raw_input())
  for i in xrange(1, t+1):
    n = int(raw_input())
    print "Case #%d: %s" % (i, solve(n))
