
def solve(N):
	n = N
	num = N
	st = set()
	i = 1
	while True:
		for ch in num:
			st.add(ch)
		if len(st) == 10:
			break
		i = i + 1
		num_x = int(n) * i
		new_str = str(num_x)
		if new_str == num:
			return "INSOMNIA"
		num = str(num_x)
	return num


T = int(raw_input())

for i in xrange(1, T + 1):
  N = raw_input()
  last_number = solve(N)
  print "Case #{}: {}".format(i, last_number)