import itertools
import time
import copy

#insomnia case
#0 x N

num_case = int(raw_input())

for i in range(num_case):
	ansr = "Case #" + str(i+1) + ": "
	n = int(raw_input())
	tmp = copy.deepcopy(n)
	if n == 0:
		ansr = ansr + "INSOMNIA"

	else:
		X = range(10)
#		print "X:" + str(X)

		K = []
		while(not K == X):

			C = list(str(n))
			K.extend(C)
#			K = list(set(K))
			K = sorted(list(set([int(k) for k in K])))
#			print "K:" + str(K)
			tp2 = copy.deepcopy(n)
			n += tmp
#			print "n:" + str(n)

		ansr = ansr + str(tp2)



	print ansr
	ansr = ""