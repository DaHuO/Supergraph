import operator


T = int(raw_input())

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(1,T+1):
	N = int(raw_input())
	arr = {}
	toks = raw_input().split(" ")
	arr1 = map(int,toks)
	for a in range(0,N):
		arr[alph[a]] = arr1[a]
	sorted_x = sorted(arr.items(), key=operator.itemgetter(1))
	# print sorted_x
	alp = []
	vals = []
	for x in sorted_x:
		alp = alp + [x[0]]
		vals = vals + [x[1]]
	# print vals ,alp
	
	alp.reverse()
	vals.reverse()

	# print alp
	# print vals
	res = "Case #" + str(t) + ":"
	for i in range(0,len(vals)-1):
		if vals[i] > vals[i+1]:
			dif = vals[i] - vals[i+1]
			for s in range(dif):
				for j in range(0,i+1):
					res = res + " " + alp[j]
					vals[j] = vals[j] - 1
	# print res
	for v in range(0, N-2):
		for q in range(0,vals[v]):
			res = res + " " + alp[v]
			vals[v] = vals[v] - 1
	# print vals
	a = alp[N-2]
	b = alp[N-1]
	for s in range(0,vals[len(vals)-1]):
		res = res + " " + a + b

	print res





