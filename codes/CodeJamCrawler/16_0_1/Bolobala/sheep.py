def solve(a):
	int_a = int(a)
	
	if int_a == 0 :
		return -1
	org = list(set(a))
	nxt_a = 0
	rnd = 2
	while len(org) < 10:
		nxt_a = int_a * rnd
		nxt = sorted(list(set(str(nxt_a))))
		org = sorted(list(set(org + nxt)))
		rnd += 1
	return nxt_a


in_file = 'A-large.in'
f = open(in_file, 'r')
nb_testcase = int(f.readline().strip('\n'))

for i in range(0,nb_testcase):
	data = f.readline().strip('\n')
	ret = solve(data)
	if ret == -1:
		ret = "INSOMNIA"
	print "Case #%d: %s"%((i+1),ret)

f.close()
