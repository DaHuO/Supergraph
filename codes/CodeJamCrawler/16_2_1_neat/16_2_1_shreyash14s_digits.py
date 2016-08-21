d = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def isN(s, i):
	j = 0
	s = s[:]
	d1 = list(d[i])
	while j < len(s):
		if s[j] in d1:
			d1.remove(s[j])
			s.remove(s[j])
		else:
			j += 1
	return not d1

def rem(s, i):
	j = 0
	d1 = list(d[i])
	while j < len(s):
		if s[j] in d1:
			d1.remove(s[j])
			s.remove(s[j])
		else:
			j += 1

def fn(s):
	i = 0
	n = ''
	s = list(s)
	while len(s) > 0:
		if isN(s, i):
			# print(''.join(s), i)
			rem(s, i)
			n += str(i)
		else:
			i += 1
	return n

def f3(s):
	l = []
	i = 0
	n = ''
	s = list(s)
	while len(s) > 0:
		if isN(s, i):
			# print(''.join(s), i)
			l.append((s[:], n, i))
			rem(s, i)
			n = n + str(i)
		else:
			while i == 9:
				if not l:
					print('err')
					return
				s = l[-1][0]
				n = l[-1][1]
				i = l[-1][2]
				l.pop()
			i += 1
	return n

t = int(input())
for i in range(1, t+1):
	s = input()
	print("Case #%d:" % i, f3(s))
