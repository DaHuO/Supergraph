def cmp(d):
	for i in d:
		s = 0
		for j in d:
			s += d[j]
		if s / d[i] >= 0.5:
			return False
	return True

def f(d):
	l = []
	ds = sorted(d)
	for i in ds:
		for j in ds:
			if i == j or i not in d or j not in d:
				continue
			d[i] -= 1
			d[j] -= 1
			t = False
			if d[i] == 0:
				d.pop(i)
				t = True
			if d[j] == 0:
				d.pop(j)
				t = True
			if not t and cmp(d):
				l.append(i+j)
			else:
				d[i] += 1
				d[j] += 1
	return l

def ok(l):
	for i in l:
		if i:
			s1 = 0
			for j in l:
				s1 += j
			if i / s1 > 0.5:
				# print(l, s1, i)
				return False
	return True

s = 0
def f2(l):
	global s
	s = sum(l)
	n = len(l)
	ans = []
	if s <= 2:
		a = []
		for i in range(len(l)):
			if l[i]:
				a.append(i)
		return [''.join(chr(65+i) for i in a)]
	# for i in range(len(l)):
	i = j = 0
	while s > 2:
		j += 1
		if j >= n:
			j = 0
			i = (i + 1) % n
		if l[i] and l[j]:
			# print(l, s, i, j)
			l[i] -= 1
			s -= 1
			if ok(l):
				ans.append(chr(65+i))
			else:
				l[j] -= 1
				s -= 1
				if ok(l):
					ans.append(chr(65+i)+chr(65+j))
				else:
					s += 2
					l[i] += 1
					l[j] += 1
	# print(l)
	a = []
	for i in range(len(l)):
		if l[i]:
			a.append(i)
			l[i] -= 1
	for i in l:
		assert(i == 0)
	return ans + [''.join(chr(65+i) for i in a)]

t = int(input())
for it in range(1, t+1):
	n = input()
	l = list(map(int, input().split()))
	# d = {chr(97+i):int(l[i]) for i in range(len(l))}
	print("Case #%d:" % it, ' '.join(f2(l)))
