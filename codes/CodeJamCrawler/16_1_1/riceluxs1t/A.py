def solve(word):
	
	res = word[0]
	for e in word[1:]:
		if e >= res[0]:
			res = e + res
		else:
			res = res + e
	return res

f_out = open('A_output.txt', 'w')
f_in = open('A-large.in', 'r')

lines = [line.strip() for line in f_in.readlines()][1:]
for idx in range(len(lines)):
	ans = solve(lines[idx])
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()