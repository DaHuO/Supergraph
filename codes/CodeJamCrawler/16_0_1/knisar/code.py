import sys
t = int(raw_input())
i = 1
while i <= t:
	n = int(raw_input())
	n1 = n
	s = [0,1,2,3,4,5,6,7,8,9]
	k = 1
	if n == 0:
		print "Case #{}: INSOMNIA".format(i)
	else:
		while s != []:
			n = n1 * k
			a = [int(j) for j in str(n)]
			for int1 in a:
				if int1 in s:
					s.remove(int1)
			k += 1
		print "Case #{}: {}".format(i,n)
	i += 1