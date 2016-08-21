import sys
import itertools
import math
def print_factors(x):
   for i in range(2, x + 1):
       if x % i == 0:
           return i
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, 101):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

for t in range(input()):
	n,q = map(int,raw_input().split())
	print "Case #1:"
	k=0
	s=[]
	count = 0
	for seq in itertools.product("01", repeat=n-2):
		l = ["".join(seq)]
		l[-1] = "1" + l[-1] + "1"
		flag = True
		t=[]
		for j in range(2,11):
			a = int(l[-1],j)
			r = list(divisorGenerator(a))
			if (len(r)<=2):
				flag = False
			t.append(r[1])
		if(flag == True):
			s.append(l[-1])
			print s[-1],
			for i in t:
				print i,
			print 
			count += 1
		if(count ==q):
			break





