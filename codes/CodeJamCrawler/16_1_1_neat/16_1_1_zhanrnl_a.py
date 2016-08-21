def f(s):
	t = s[0]
	for c in s[1:]:
		t1 = t + c
		t2 = c + t
		if t1 < t2:
			t = t2
		else:
			t = t1
	return t

n = int(raw_input())
for i in range(n):
	s = raw_input()
	print "Case #{}: {}".format(i+1, f(s))
