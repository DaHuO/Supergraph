
def find_answer(x):
	if x == 0:
		return 'INSOMANIA'
	
	has_seen = {}
	str_x = str(x)
	for e in str_x:
		has_seen[int(e)] = True

	for i in range(2, 1000):
		str_x = str(i*x)
		for e in str_x:
			has_seen[int(e)] = True
		if len(has_seen) == 10:
			return i*x
	return 'CANT FIND WITHIN 1000'


f_out = open('A_output.txt', 'w')
f_in = open('A-small-attempt0.in', 'r')

lines = [line.strip() for line in f_in.readlines()][1:]
for idx in range(len(lines)):
	ans = find_answer(int(lines[idx]))
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()