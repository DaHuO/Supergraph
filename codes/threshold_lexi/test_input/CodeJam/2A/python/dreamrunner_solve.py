# Order P, R, S


def match(o):
	if o == "P":
		return ["P", "R"]
	elif o == "R":
		return ["R", "S"]
	elif o == "S":
		return ["P", "S"]


def cal_n(N):
	l = ["P"]
	for i in range(N):
		nl = []
		for item in l:
			nl += match(item)
		l = nl
	c_p = 0
	c_r = 0
	c_s = 0
	for i in l:
		if i == "P":
			c_p += 1
		if i == "R":
			c_r += 1
		if i == "S":
			c_s += 1
	return [c_r, c_p, c_s], l


def refine(s):
	if len(s) == 2:
		a, b = s
		if a > b:
			a, b = b, a
		return a + b
	hls = len(s) // 2
	a, b = s[: hls], s[hls:]
	a = refine(a)
	b = refine(b)
	if a > b:
		a, b = b, a
	return a + b


T = int(input())

for test in range(1, T+1):
	print("Case #" + str(test) + ": ", end="")
	n, r, p, s = [int(i) for i in input().split()]
	arr, ll = cal_n(n)
	a_r = None
	a_p = None
	a_s = None
	r_done = False
	p_done = False
	s_done = False
	if r == arr[0]:
		a_r = "R"
		r_done = True
	elif p == arr[0]:
		a_r = "P"
		p_done = True
	elif s == arr[0]:
		a_r = "S"
		s_done = True
	if not r_done and r == arr[1]:
		a_p = "R"
		r_done = True
	elif not p_done and p == arr[1]:
		a_p = "P"
		p_done = True
	elif not s_done and s == arr[1]:
		a_p = "S"
		s_done = True
	if not r_done and r == arr[2]:
		a_s = "R"
	elif not p_done and p == arr[2]:
		a_s = "P"
	elif not s_done and s == arr[2]:
		a_s = "S"

	# print(arr, r, p, s)
	# print(a_r, a_p, a_s)

	if a_r is None or a_p is None or a_s is None:
		print("IMPOSSIBLE")
	else:
		ans = ""
		for i in ll:
			if i == "R":
				ans += a_r
			if i == "P":
				ans += a_p
			if i == "S":
				ans += a_s
		ans = refine(ans)
		print(ans)


