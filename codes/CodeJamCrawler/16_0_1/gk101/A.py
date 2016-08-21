def find_all_digits(N):
  if N == 0:
    return 'INSOMNIA'
  numset = set()
  
  num = 0
  while len(numset) < 10:
    num += N
    add_all_digits(num, numset)
  return str(num)

def add_all_digits(num, numset):
  for n in str(num):
    numset.add(int(n))
  
T = int(raw_input())
for i in xrange(T):
  N = int(raw_input())
  print "Case #%d: %s" % (i + 1, find_all_digits(N))