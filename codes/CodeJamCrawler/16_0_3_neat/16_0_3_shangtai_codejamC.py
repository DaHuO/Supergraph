T = int(raw_input())
N, J = map(int, raw_input().split())

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def primefactors(x):
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            return loop
        else:
            loop+=1


print "Case #1:"
j=0
for candidate in xrange(2**(N-2)):
    candidate=candidate<<1
    candidate+=(1+(1<<(N-1)))
    candidate="{0:b}".format(candidate)
    factorlist=[candidate]
    for base in xrange(2,11):
        candidatebase=int(candidate,base)
        if is_prime(candidatebase):
            break
        else:
            factorlist.append(primefactors(candidatebase))
    if len(factorlist)==10:
        j+=1
        for i in factorlist:
            print i,
        print 
    if j==J:
        break



