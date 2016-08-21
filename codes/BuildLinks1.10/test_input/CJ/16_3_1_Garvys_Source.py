T = int(input())

def mySum(l):
	res = 0
	for i in l:
		res += i[1]
	return res

def myMax(l):
	m = 0
	for i in l:
		m = max(m,i[1])
	return m

for t in range(T):
	N = int(input())
	s = list(map(int,input().split()))
	l = list()
	for i,c in enumerate(s):
		l.append([i,c])

	res = []

	while mySum(l) > 0:

		l.sort(key=lambda x: x[1])

		s =[]

		if l[-1][1] != 0:
			l[-1][1] -= 1
			s.append(chr(l[-1][0]+ord('A')))

		l.sort(key=lambda x: x[1])
		if l[-1][1] != 0:
			l[-1][1] -= 1

			m = myMax(l)
			n = mySum(l)

			if n > 0 and m / n > 0.5:
				l[-1][1] += 1
			else:
				s.append(chr(l[-1][0]+ord('A')))

		res.append(''.join(s))
	print("Case #{}: {}".format(t+1,' '.join(res)))

