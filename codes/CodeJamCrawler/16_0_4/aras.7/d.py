import math

for test in range(1, int(raw_input()) + 1):
	K, C, S = map(int, raw_input().split())
	
	answer = []
	elements = K ** C

	r = elements / S

	for i in range(1, S+1):
		answer.append(i*r)

	print "Case #{}: {}".format(test, ' '.join(map(str, answer)))
