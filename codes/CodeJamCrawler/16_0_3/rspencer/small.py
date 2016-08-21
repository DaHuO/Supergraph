# Run with length as first argument and number to find as second
import sys
primes = []
minDivisor = [1000000000 for i in xrange(100000)]
for i in xrange(2,100000):
  for j in xrange(i,100000,i):
    minDivisor[j] = min(minDivisor[j],i)
for i in xrange(2,100000):
  if minDivisor[i] == i:
    primes.append(i)

count = 0
print "Case #1:"
begin = (1<<int(sys.argv[1])-1)+1
end = 1<<(int(sys.argv[1]))
i = begin
while i < end:
  divs = [-1 for j in xrange(9)]
  for base in xrange(2,11):
    x = int(bin(i)[2:],base)
    for p in primes:
      if x%p==0 and x!=p:
        divs[base-2]=p
        break
  if -1 not in divs:
    print bin(i)[2:],' '.join(map(str,divs))
    count += 1
  if count >=int(sys.argv[2]): break;
  i += 2
