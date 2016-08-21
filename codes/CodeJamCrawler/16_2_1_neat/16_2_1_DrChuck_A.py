t = int(raw_input())
for case in range(1,t+1):
	s = raw_input()
	cdict = {'Z':0, 'W':0,'U':0,'X':0,'G':0,'O':0,'H':0,'F':0,'S':0,'I':0}
	for c in s:
		if c not in cdict:
			cdict[c] = 0
		cdict[c] += 1
	ans = [0 for i in range(10)]

	ans[0] = cdict['Z']
	ans[2] = cdict['W']
	ans[4] = cdict['U']
	ans[6] = cdict['X']
	ans[8] = cdict['G']
	ans[1] = cdict['O'] - ans[0] - ans[2] - ans[4]
	ans[3] = cdict['H'] - ans[8]
	ans[5] = cdict['F'] - ans[4]
	ans[7] = cdict['S'] - ans[6]
	ans[9] = cdict['I'] - ans[5] - ans[6] - ans[8]
	#print "Case #" + str(case) + ":", ans
	rlst = []
	for i in range(10):
		if ans[i] > 0:
			rlst +=[str(i) for j in range(ans[i])]
	print "Case #" + str(case) + ":", "".join(rlst)
