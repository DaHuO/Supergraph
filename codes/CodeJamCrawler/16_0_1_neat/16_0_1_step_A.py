import os, sys

T = int(input())
for t in range(T):
	res = "INSOMNIA"
	N = int(input())
	seen = {}
	digits = {}
	if N != 0:
		i = 1
		while 1:
			v = i * N
			vstr = str(v)
			for ch in vstr:
				if not ch in digits:
					digits[ch] = 1
			seen[vstr] = 1

			# print("i:{0} v: {1}".format(i,v))
			if len(digits) == 10:
				res = vstr
				break
			i+= 1

	print("Case #{0}: {1}".format(t+1, res ) )
