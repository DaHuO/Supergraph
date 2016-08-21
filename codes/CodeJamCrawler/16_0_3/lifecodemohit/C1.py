def check_prime(n) :
	if n < 2 :
		return 0
	else :
		for i in xrange(2, 1000) :
			if n%i == 0:
				return i
		return 0


t = int(raw_input())
n, k = raw_input().split()
n = int(n)
k = int(k)

print "Case #1:"

for i in xrange(2**(n-1), 2**n) :
	if k <= 0 :
		break
	if i%2 != 0 :
		v1 = []
		for base in xrange(2, 11) :
			answer = 0
			val = 1
			for j in xrange(0, n) :
				if (i & (1 << j)) :
					answer = answer + val
				val = val*base
			check_pm = check_prime(answer)
			if check_pm > 1 :
				v1.append(check_pm)
			else :
				break
		if len(v1) == 9 :
			res = ""
			for j in xrange(0, n) :
				if (i & (1 << (n-1-j))) :
					res = res + '1'
				else :
					res = res + '0'
			res = res + " "
			for j in xrange(0, 9) :
				res = res + str(v1[j]) + " "
			print res
			k = k-1
