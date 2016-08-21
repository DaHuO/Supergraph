# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def numbers(n):
    res = []
    while n != 0 :
        tmp = n % 10
        res.append(tmp)
        n /= 10
    return res

def test(d):
    for i in xrange(0,10):
        if i not in d:
            return False
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  ha = int(raw_input())
  d = set()
  n = ha
  while (True):
      if ha == 0:
          break
      tmp = numbers(n)
      for x in tmp:
          d.add(x)
      if test(d):
          break
      else:
          n += ha
  if ha == 0:
      print "Case #{}: INSOMNIA".format(i)
  else:
      print "Case #{}: {}".format(i, n)
  # check out .format's specification for more formatting options