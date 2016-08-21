# imports

import math

# code
def factor(n):
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return i
  return -1

def divisors(s):
  l = []
  for i in xrange(2, 11):
    num = int(s, i)
    fac = factor(num)
    if fac == -1:
      return None
    else:
      l.append(fac)
  return l

def jamcoins(N, J):
  d = {}
  for n in xrange(2 ** (N - 2)):
    s = format((n * 2) + 1 + (2 ** (N - 1)), '0{}b'.format(N))
    dv = divisors(s)
    if dv:
      d[s] = dv
    if len(d) >= J:
      break
  return d

if __name__ == "__main__":
  g = open("output3", "w")
  with open("C-small-attempt1.in") as f:
    num_cases = 0
    read_num_cases = False
    c = 1
    for line in f:
      if not read_num_cases:
	read_num_cases = True
	num_cases = int(line)
      else:
	g.write("Case #" + str(c) + ":\n")
	inputs = line.split(" ")
	d = jamcoins(int(inputs[0]), int(inputs[1]))
	for k, v in d.iteritems():
	  g.write(k)
	  for i in v:
	    g.write(" " + str(i))
	  g.write("\n")
	c += 1
  g.close()