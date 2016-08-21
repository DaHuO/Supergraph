fid = open('input.txt')
T = fid.readline().strip()
fout = open('output.txt','w')

import numpy as np

#Very inefficient, but I don't think it will matter...
#We can ignore 2, because all our numbers are odd
def small_factor(x):
    xf = float(x)
    for j in xrange(3,int(np.ceil(np.sqrt(x))),2):
        a = xf/j
        if a == np.ceil(a):
            return j
    return 1


#In base 2, the factors will be the same.  We do base 2, and then we just
#convert it

#This takes a binary string and interprets it as base b
#int(s,b)

#This takes a number and converts it to a binary string
#"{0:b}".format(5)



def check_soln(s, div):
  for i in range(len(div)):
    b = 2+i
    x = int(s,b)/float(div[i])
    if x != np.ceil(x):
      print "ERR: %s, base %d, divisor %d" % (s,b,div[i])


#Only one of the factors works sometimes (since the other needs a b-1 instead
# of a 1)
#Even this approach doesn't work all the time, but it's lazy and there are
#enough results that do work.
def tmp(s, b, f1,f2):
    x1 = int(s,b)/float(int(f1,b))
    x2 = int(s,b)/float(int(f2,b))
    if x1 == np.ceil(x1):
      return int(f1,b)
    elif x2 == np.ceil(x2):
      return int(f2,b)
    else: 
      #I'll just throw these away
      return -1


def get_solns(N,J):
  solns = []
  #Generate a bunch of trial strings
  for r in xrange(2**(N-2)):
    #Form our trial number
    s = '1' + format(r,'0'+str(N-2)+'b') + '1'
    #Figure out what the number is in binary
    k = int(s,2)
    #Find a factor of the number, or see if it is prime
    fac = small_factor(k)
    if fac == 1:
      #This one was prime, keep going
      continue
    #Otherwise, we are good!
    #Convert the factor to binary
    fac_str = format(fac, 'b')
    fac_str2 = format(k/fac,'b')
    
    #One of these will be the right divisor in every base
    #divisors = [int(fac_str,b) for b in range(2,11)]
    divisors = [tmp(s,b,fac_str,fac_str2) for b in range(2,11)]
    #divisors = [small_factor(int(s,b)) for b in range(2,11)]
    if min(divisors) < 1:
      continue
    solns.append((s, divisors))
    check_soln(s,divisors)
    if len(solns)==J:
      break
  return solns


for i,line in enumerate(fid):
    line = line.strip()
    if len(line)==0:
        continue
    N, J = [int(x) for x in line.split(' ')]

    solns = get_solns(N,J)
   
    fout.write('Case #%d:\n' % (i+1))
    for soln in solns:
        fout.write(soln[0] + ' ' + ' '.join([str(d) for d in soln[1]])+'\n')
