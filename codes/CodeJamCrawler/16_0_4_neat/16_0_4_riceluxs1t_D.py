def solve(k, c, s):
	# since k == s for the small input, you can just check the first s tiles
	# and see if any of them contains G in it.
	if k != s:
		return 'IMPOSSIBLE'
	return ' '.join(map(str, range(1, s+1)))

f_out = open('D_output.txt', 'w')
f_in = open('D-small-attempt0.in', 'r')

lines = [line.strip() for line in f_in.readlines()][1:]
for idx in range(len(lines)):
	k, c, s = map(int, lines[idx].split())
	ans = solve(k, c, s)
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()


