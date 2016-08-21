
def solve(S):
	inp = S
	if S.count('+') == len(S):
		return 0

	boundary = S.rfind("-")

	new_S = S[0:boundary+1]
	num_steps = 0

	while True:
		same_count = 1
		new_version = ""

		for s in new_S[1:]:
			if s == new_S[0]:
				same_count = same_count + 1
			else:
				break
		if same_count == len(new_S) and new_S[0] == "+":
			break

		if new_S[0] == "+":
			new_version = "-"
		else:
			new_version = "+"

		new_S = new_version * same_count + new_S[same_count:]
		num_steps = num_steps + 1
	return num_steps


T = int(raw_input())

for i in xrange(1, T + 1):
  S = raw_input()
  num_of_steps = solve(S)
  print "Case #{}: {}".format(i, num_of_steps)