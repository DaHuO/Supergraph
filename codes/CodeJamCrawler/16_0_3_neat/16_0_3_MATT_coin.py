import functools
import operator

#t = int(raw_input())  # read a line with a single integer
#for i in xrange(1, t + 1):
#  N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case, (16, 50) and (32, 500)
#  output(i,N,J)

def output(i,N,J):
  print "Case #{}:".format(i)
  for jj in xrange(J):
      binpol = ''.join(str(e) for e in find_poly(N,jj))
      print "{} {} {} {} {} {} {} {} {} {}".format(binpol, 2+1, 3+1, 4+1, 5+1, 6+1, 7+1, 8+1, 9+1, 10+1) # divisors are all b+1

def find_poly(N, i):
    cc = bits(i)
    if 2*len(cc) > N-4:
        raise ValueError(i, " is bigger than number of valid sparse patterns for " , N)
    poly = [0]*N
    poly[0]=1
    poly[1]=1
    poly[N-1]=1
    poly[N-2]=1
    for k in xrange(len(cc)):
        poly[2*k+2]=cc[k]
        poly[2*k+3]=cc[k]
    return(poly)

def test_poly(poly):
    return([eval(poly,b)%(b+1) for b in xrange(2,11)])

def eval(poly, b):
    return(functools.reduce(operator.add, [poly[i]*b**i for i in xrange(0,len(poly))]))

def bits(i):
    l = [i%2]
    i = i//2
    while i != 0:
        l.append(i%2)
        i = i//2
    return(l)

      


        



