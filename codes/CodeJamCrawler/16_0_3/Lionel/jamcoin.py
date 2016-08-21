import sys

def primes_sieve2(limit):
    a = [True] * limit                          
    a[0] = False
    a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
	        # Mark factors non-prime
                a[n] = False

def gen_primes(limit):
    s = []
    for aa in primes_sieve2(limit):
        s.append(aa)
    return s

def num2bits(k, dig):
    ar = []

    base = pow(2, dig-3)
    for i in xrange(dig-2):
	ar.append(k/base)
	k %= base
	base /= 2
    return ar

def combo_num(ar, d, dig):
    base = pow(d, dig-1) + 1

    aa = dig-2
    for elem in ar:
	if elem > 0:
	    base += pow(d, aa)
	aa -= 1
    return base

def is_prime(num, ps):
    for elem in ps:
	if num > elem and num % elem == 0:
	    return elem
    return 0

def ar2str(ar):
    ss = "1"
    for elem in ar:
	ss += str(elem)
    ss += "1"
    return ss

def main():
    
    f = open(sys.argv[1])
    t = int(f.readline().strip())

    ps = gen_primes(100000)
    
    for kk in xrange(t):
	    line = f.readline()
	    sp = line.strip().split()
	    n = int(sp[0])
	    j = int(sp[1])

	    print "Case #"+str(kk+1)+":"

	    i = 0
	    
	    for p in xrange(0, pow(2, n-2)):
		ar = num2bits(p, n)
		flag = True
		intp = []
		for d in xrange(2, 11):
		    num = combo_num(ar, d, n)	
		    bint = is_prime(num, ps)
		    if bint > 0:
			intp.append(bint)
		    else:
			flag = False
			break
		if flag:
		    pstr = ar2str(ar)+" "
		    for l in xrange(len(intp)):	
			pstr += str(intp[l])
			if l < len(intp)-1:
			    pstr += " "
		    print pstr
		    i += 1

		    if i >= j:
			break

    f.close()

if __name__ == "__main__":
    main()
