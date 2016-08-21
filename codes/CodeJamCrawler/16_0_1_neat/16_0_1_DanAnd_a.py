T=int(raw_input())

Ns = []
for t in xrange(T):
  Ns.append(int(raw_input()))

def test(n):
  if n == 0: return 'INSOMNIA'
  a = n
  digits = set(str(a))
  while len(digits) < 10:
    a += n
    digits |= set(str(a))
  return str(a)

for t, n in enumerate(Ns):
  print "Case #{}: {}".format(t+1, test(n))  
