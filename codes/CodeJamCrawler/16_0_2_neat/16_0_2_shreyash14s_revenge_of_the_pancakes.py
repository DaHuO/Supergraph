def flip(s, i=None):
	# s[:i] = s[:i].replace('-', '.')
	# s[:i] = s[:i].replace('+', '-')
	# s[:i] = s[:i].replace('.', '+')
	if not i:
		i = len(s)
	a = s[:i].replace('-', '.')
	a = a.replace('+', '-')
	a = a.replace('.', '+')
	a += s[i:]
	return a

def f(s):
	c = 0
	l = len(s)
	i = s.rfind('-')
	while i >= 0:
		#if i == l-1:
		#	s = flip(s)
		#else:
		s = flip(s, i+1)
		# print(s, i)
		c += 1
		i = s.rfind('-')
	return c

# print(flip('-+', '-+'.rfind('-')-1), "---".rfind('+'))
t = int(input())
for i in range(1, t+1):
	s = input()
	print("Case #%d:" % i, f(s))
