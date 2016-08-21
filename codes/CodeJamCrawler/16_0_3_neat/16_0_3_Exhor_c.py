import numpy, time

def findFactor(x, primes):
  iscoin = True
  facs = [-1 for i in range(11)]
  for b in range(2,11):
    isprime = True
    for potfac in primes:
      if potfac ** 2 > x[b]:
        break
      if divmod(x[b], potfac)[1] == 0:
        facs[b] = potfac
        isprime = False
        break
    if isprime == True:
      iscoin = False
      break
  return iscoin, facs

f = open('outputsmall.txt','w')
fi = open('csmall.txt','r')

N = 16
n = 2**N
sieve = numpy.ones(n/2, dtype=numpy.bool)
for i in xrange(3,int(n**0.5)+1,2):
  if sieve[i/2]:
    sieve[i*i/2::i] = False
primes = 2*numpy.nonzero(sieve)[0][1::]+1
print 'primes = ' + str(primes[0:12])

starttime = time.time()

T = int(fi.readline())
for k in range(1,T+1):
  NJ = [int(r) for r in fi.readline().split(' ')]
  print NJ
  N = NJ[0]
  J = NJ[1]

  f.write('Case #'+str(k)+':\n')
  ff = 1 + 2**(N-1)
  #inbase = [1+i**(N-1) for i in range(0,11)]  # 1000.001 for each base 2..10
  #print inbase
  ncoins = 0
  for x in xrange(ff,2**N-1,2):
    binx = bin(x)[2:]
    inbase = [0 for i in range(0, 11)]
    for e in range(N):
      if binx[-(e + 1)] == "1":
        for b in range(2, 11):
          inbase[b] = inbase[b] + b ** e
    #print binx + ' = ' + str(inbase)
    for n in range(1,len(binx)+1):
      if binx[-n] != "1":
        break
    n = n - 1
    # print 'n = ' + str(n)
    if n == N:
      break
    iscoin, baseFactors = findFactor(inbase, primes)
    #print 'base factors = ' + str(baseFactors)
    if iscoin:
      ncoins = ncoins + 1
      print str(ncoins) + ' at ' + str(time.time() - starttime)
      f.write(binx + ' ' + str(baseFactors[2:11]).replace(',','').replace('[','').replace(']','') + '\n')
    if ncoins == J:
      print 'Enough coins found'
      break
    # next potential coin, update in all bases

      #j = (b**(n+1) - 2*(b**n) + 1)/(b - 1) + b
      #inbase[b] = inbase[b] + j

