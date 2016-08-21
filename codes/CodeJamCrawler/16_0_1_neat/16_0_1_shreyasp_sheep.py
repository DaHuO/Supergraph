import sys

def total(list):
  sum = 0
  for n in list:
    sum += n
  return sum

def main(argv):
  t = int(raw_input().strip())

  for ii in xrange(t):
    c = 1
    flags = [0] * 10
    orig_n = int(raw_input().strip())
    if orig_n == 0:
      print "Case #%s: INSOMNIA" % (ii+1)
      continue

    n = orig_n
    nn = n
    while total(flags) < 10:
      nn = c * orig_n
      n = nn
      c += 1
      while n:
        r = n%10
        flags[r] = 1
        n = n/10
    print "Case #%d: %d" % (ii+1, nn)

if __name__ == "__main__":
  main(sys.argv)
