raw_input()

n , j = map(int, raw_input().split(" "))
print 'n=', n, 'j=', j

MAX_TD = 100

def get_divisor(x):
#  print 'x=',x
  for i in xrange(2, MAX_TD):
    if x % i == 0:
      return i
    if i * i > x:
      return None
  return None

arr = []
for i in xrange(2**(n-1), 2**n+1):
  if i%2 == 0:
    continue
#  print 'i=', i
  s = "{0:b}".format(i)
#  print 's = ', s
  divisors = [get_divisor(int(s, base=b)) for b in range(2, 10+1)]
  if None in divisors:
    continue
  arr.append( (s, divisors))
  if len(arr) == j:
    break

print 'Case #1:'
for k,v in arr:
  print k,
  for vv in v:
    print vv,
  print
