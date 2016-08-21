t = input()
m = []
for i in xrange(t):
	n = input()
	m.append(map(int, raw_input().split()))
for i in xrange(len(m)):
	t = m[i]
	ans = ""
	while(sum(t) > 0):
		idx1 = 0
		idx2 = 1
		for j in xrange(len(t)):		
			if t[j] > t[idx1]:
				idx2 = idx1
				idx1 = j
			elif t[j] > t[idx2]:
				idx2 = j
		t[idx1] -= 1
		t[idx2] -= 1
		mx = max(t)
		flag = 0
		#print t, idx1, idx2
		if mx > sum(t) - mx:
			t[idx2] += 1
			flag = 1
		if flag:
			ans += chr(65 + idx1) + " "
		else:
			ans += chr(65 + idx1) + chr(65 + idx2) + " "
	print "Case #" + str(i + 1) + ": " + ans.rstrip()
