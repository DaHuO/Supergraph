T = input()

for i in xrange(T):

	N = input()
	P = map(int, raw_input().split())

	d = {}
	di = {}

	count = 0
	for j in xrange(N):
		d[chr(j+65)] = P[j]
		count += P[j]

	#print d

	ans = ""
	while True:
		if count == 3:
			break
		maxval, maxindex = -1, -1
		maxval2, maxindex2 = -1, -1
		for j in d:

			if maxval == d[j]:
				maxval2 = d[j]
				maxindex2 = j

			if maxval < d[j]:
				maxval = d[j]
				maxindex = j

		if maxval == 0:
			break

		if maxindex2 != -1:
			d[maxindex2] -= 1
			count -= 1
		d[maxindex] -= 1
		count -= 1
		ans += maxindex + [maxindex2,""][maxindex2 == -1] + " "

	if count == 3:
		for j in d:
			if d[j] > 0:
				#print "--", j
				ans += j + " "
				count -= 1
				d[j] -= 1
				break
		#if count == 2:
		for j in d:
			if d[j] > 0:
			#	print "---", j
				ans += j

	print "Case #" + str(i+1) + ": " + ans