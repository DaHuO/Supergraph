#codejam 4/8/2016
import math #as m
import time
#import codejam
import sys
import os
import random
sys.setrecursionlimit(205) #sometimes we need 1000 max

cwd = os.getcwd()
filename = cwd+r'\c-test.in.txt'
filename = cwd+r'\c-small-attempt0.in'
filename = cwd+r'\c-large.in'
#filename = cwd+r'\c-small-practice.in'
foutname = filename.replace(".in",".out")

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def ceildiv(x, d):#like x//d but ceiling, for positives only
    return (x + (d-1)) // d

def baseN(num,b):
    """Return num as a string in base b"""
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

#print baseN(16,2),"=10000 ?"
#print baseN(28,3),"=1001 ?"

powers = [[pow(b, k) for k in range(32)] for b in range(11)]  #powers[5] is the powers of 5: 5**0, 5**1, 5**2 etc.  powers[a][b] is a**b = pow(a,b)

def binfmbase(binlis, radix): #digits 0 or 1
    "converts list of 1's and 0's in base 'radix' to a number"
    ans = 0
    for k,digit in enumerate(reversed(binlis)):
        if digit: ans += powers[radix][k]
    return ans
def fmbase(lis, radix): #any digits
    "converts list in base 'radix' to a number"
    ans = 0
    for digit in lis:
        ans *= radix
        ans += digit
    return ans
def fmbasestr(strdigits, radix): #any digits
    "converts str in base 'radix' to a number"
    ans = 0
    for digit in strdigits:
        ans *= radix
        ans += ord(digit) - ord('0')
    return ans


primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29
            , 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
            , 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149
            , 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281
            , 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439
            , 443, 449, 457, 461, 463, 467, 479, 487]
#use addNprimes(143) to add primes up to 997 (takes 47 msec)

primedict={}    # empty dictionary
for a in primelist: primedict[a]=1  # put them all into dictionary
# remainders when divided by 210 that have a chance of being prime
p210 = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199] #len=46
# for example, we don't have 9 in there because if n is divisible by 210, n+9 is
# not prime (because n is divisible by 3, and so is n+9)

def getfactor_lazy(n):
    if primedict.get(n,0): return 1 #prime
    for test in primelist:
        if n%test==0: return test #factor
    return 1 #act like it is a prime -- which for codejam is good enough

def isprime(n, maxtries=10000):
    """Returns 1 if n is prime, and a factor otherwise"""

    if primedict.get(n,0):  # yes, in dictionary
        return 1            # so it's a prime!
    #want factor, so stop this: if n<primelist[-1]: return 0    # small enough to be in dictionary, so not prime
    #starttime = time.clock()
    for test in primelist:
        if n % test==0: #was: if test*(n/test) == n:
            return test # divisible by this prime, so not prime
    if n<(primelist[-1]**2):# can't possibly be a factor, too big.  Must be prime.
        primedict[n]=5      # remember this prime, even though not contiguous
        return 1   # we tested all possible factors, so prime
    tries=1
    while 1:                # keep trying higher and higher primes
        test=primelist[-1]+2   # next number to test to see if it's prime
        # recursive, but that's ok because inner call only needs sqrt as big primes
        while not isprime(test): test += 2  # search odd numbers for a prime
        primelist.append(test)
        primedict[test]=1
        
        #if test*(n/test) == n: return test #factor
        if n % test == 0: return test # factor
        if n < (test**2): return 1
        #dlta = (time.clock()-starttime)
        #if dlta > maxseconds:
        #    raise Exception("isprime("+`n`+") took longer than "+`maxseconds`+" seconds.")
        if tries>maxtries: raise Exception("isprime too many tries (%d)"%(maxtries,))
        
def addNprimes(n):
    """puts n more primes onto primelist

    Adding in a batch is only slightly faster than one at a time
    """
    nadded=0
    
    while nadded < n:
        j=primelist[-1]+2   # next number to test to see if it's prime
        while isprime(j)>1: j += 2 #keep going if it has a factor
        primelist.append(j)
        primedict[j]=1
        nadded += 1
    #print "New primes: ",primelist[-nadded:]

    
def num2bin(num,numdigits):
    """number to vector of digits in binary"""
    ans = [0] * numdigits
    for r in xrange(numdigits): #will fill ans from right to left
        if num%2==1: ans[numdigits-1-r]=1
        num = num//2 #discard remainder just used above
    if num>0: raise Exception("Not enough digits allowed for %d! digits allowed=%d" %(num,numdigits))
    return ans

def nextbin(binvec,dbg=0): #find next binary number, updating in place, leaving low bit=1.  Returns power added, always 1 so far
    #find right-most zero and change it to a 1, then take all 1's to its right and zero them except right-most
    for k in range(len(binvec)-2,0,-1):
        if binvec[k]==0:
            binvec[k] += 1
            for j in range(k+1,len(binvec)-1): binvec[j]=0
            return 1 #power of radix added
    raise "all 1's!!"


def sol1(N,J,dbg=1):#N=length of Jamcoin, J=number of them to make
    if N<=0: raise "must be non-zero len"
    if N==1: binv = [1]
    else: binv = [1] + [0]*(N-2) + [1] #smallest possible jamcoin, will be updated
    build = []
    Jlim=J
    if Jlim<>J: print "test using limited J cases!"
    for jj in range(Jlim):
        result = sol1b(binv, dbg)
        #check result
        if dbg:#check
          z1, factors, primect = result
          for r in range(2,11):
            v = fmbasestr(z1, r)
            fact = factors[r-2]
            if v%fact==0: pass #works
            else: raise Exception("not a factor! "+str(v)+" % "+str(fact)+" (radix "+str(r)+")")
        build.append(result)
        if jj%20==1: print "sol1 ",jj,binv
        if sum(binv)==len(binv):
            print "End of possibilities for this many bits"
            break
        else: ignorepower = nextbin(binv) #we don't care about value here
        
    return build

def sol1b(binv, dbg=1): #make one jamcoin
    factors = [1]*11 # we only use [2] to [10]
    vs = [0,0]+[binfmbase(binv,radix) for radix in range(2,11)] #values of binv in each radix
    #dbg_vs = " ".join([str(k)+":"+str(v) for k,v in enumerate(vs)])
    #if dbg: print "dbg_vs="+dbg_vs
    fact, tries = 1,1
    primecount=0
    while fact==1:
        tries += 1
        if tries>1000: raise "over n tries "+str(tries)
        for radix in range(2,11):
            fact = getfactor_lazy(vs[radix]) #harmless if it lies and says it is prime when it is not, we just go onto another binv (assuming lots)
            #print "radix=",radix,"vs=",vs[radix],fact,"\n" if fact==1 else ""
            if fact>=vs[radix] or vs[radix]%fact<>0: raise Exception("factor trouble %d, %d" % (vs[radix],fact))
            factors[radix] = fact
            if fact==1:
                primecount += 1
                break #something not prime, will fix below by trying a new binv
        if fact>1: #done - all radices work
            return ''.join([chr(48+b) for b in binv]) , factors[2:], primecount
        #something was prime, need to try again
        ignorepower = nextbin(binv) #update in place
        for r in range(2,11):
            vs[r] = binfmbase(binv,r)
        #dbg_vs = " ".join([str(k)+":"+str(v) for k,v in enumerate(vs)])+ "#2"
    raise "never gets here sol1b"
    #answer and path to answer


        
dbg=0
if dbg: print "T=",T
if 1:
  t0 = time.time()
  sumz = 0
  for iit in range(1,T+1):
    rawline = FILE.readline()
    if rawline is None or rawline=='' or rawline=='\n':
        print "EOF reached before T=",T," - quit early. i=",iit
        break
    rawline = rawline.rstrip().split(' ') #no newline at end
    nparams=2
    N,J = [int(a) for a in rawline[:nparams]]
    if len(rawline)>nparams: manual_ans = rawline[nparams] #manually computed answer as string
    else: manual_ans = None
    
    if dbg: print "Attempt Case #" + str(iit)+": N,J,manual_ans=",N,J,manual_ans

    codepath = None
    results = sol1(N,J,dbg)

    msg = ['Case #' + str(iit) + ':']
    for z1, factors, primect in results:
        msg.append(z1+ " " + (" ".join([str(f) for f in factors])))
        if dbg and primect>0: print z1+" primect=",primect

    if not dbg and iit%10==1: print "\n".join(msg)
    FOUT.write("\n".join(msg) + "\n")
    if dbg: print ""
  print "finished",T,"cases,", round(time.time() - t0,3),"s, sumz:",sumz
FOUT.close()
FILE.close()

def testme(bitstr, radix, factor):
    v = fmbasestr(bitstr,radix)
    print "b='%s'; v=%d; r=%d; f=%d; v_mod_f=%d " % (bitstr, v, radix, factor, v%factor),"OK!" if v%factor==0 else "Bad---------"
    
