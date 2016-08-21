
def get_ans(ls):
	dct = {}
	for l in ls:
		# print l
		for el in l:
			if str(el) not in dct:
				dct[str(el)] = 0

			dct[str(el)] += 1


	l = []
	for k in dct.keys():
		if dct[k] %2 != 0:
			l.append(k)
	
	# print dct
	# print l

	l = [ int(ll) for ll in l]
	l.sort()

	sl = ''
	for el in l:
		sl += (str(el) + ' ')

	# print sl
	# s = raw_input()


	return sl

f = open("B-large.in" , "r")

lines = f.readlines()

cnt = 0 
T = int(lines[cnt])

for i in range(T):
	cnt += 1
	N = int(lines[cnt])

	lists = []
	for j in range(2*N-1):
		cnt += 1
		ln = lines[cnt].split("\n")[0].split()
		lists.append(ln)

	ans = get_ans(lists)
	ans = "Case #"+str(i+1)+": "+str(ans)
	print ans



