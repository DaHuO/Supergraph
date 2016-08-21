def f(s):
	a = s[0]
	for i in s[1:]:
		if ord(i) >= ord(a[0]):
			a = i + a
		else:
			a = a + i
	return a

t = int(input())
for i in range(1, t+1):
	s = input()
	print("Case #%d:" % i, f(s))