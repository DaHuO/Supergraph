text_file = open("output.txt", "w")
lines = [line.rstrip('\n') for line in open('input.txt')]
t = int(lines[0])
for k in range(1,t + 1):
	ans = [0 for i in range(0,10)]
	a = [0 for i in range(0,26)]
	n0 = [25,4,17,14]
	n1 = [14,13,4]
	n2 = [19,22,14]
	n3 = [19,7,17,4,4]
	n4 = [5,14,20,17]
	n5 = [5,8,21,4]
	n6 = [18,8,23]
	n7 = [18,4,21,4,13]
	n8 = [4,8,6,7,19]
	n9 = [13,8,13,4]
	s = lines[k]
	for i in range(0,len(s)):
		a[ord(s[i])-65] += 1
	while (a[25] != 0):
		for i in range(0,len(n0)):
			a[n0[i]] -= 1
		ans[0] += 1
	while(a[22] != 0):
		for i in range(0,len(n2)):
			a[n2[i]] -= 1
		ans[2] += 1
	while (a[20] != 0):
		for i in range(0,len(n4)):
			a[n4[i]] -= 1
		ans[4] += 1
	while (a[23] != 0):
		for i in range(0,len(n6)):
			a[n6[i]] -= 1
		ans[6] += 1
	while (a[18] != 0):
		for i in range(0,len(n7)):
			a[n7[i]] -= 1
		ans[7] += 1
	while (a[6] != 0):
		for i in range(0,len(n8)):
			a[n8[i]] -= 1
		ans[8] += 1
	while (a[14] != 0):
		for i in range(0,len(n1)):
			a[n1[i]] -= 1
		ans[1] += 1
	while (a[13] != 0):
		for i in range(0,len(n9)):
			a[n9[i]] -= 1
		ans[9] += 1
	while (a[21] != 0):
		for i in range(0,len(n5)):
			a[n5[i]] -= 1
		ans[5] += 1
	while (a[4] != 0):
		for i in range(0,len(n3)):
			a[n3[i]] -= 1
		ans[3] += 1
	ans_s = ''
	for i in range(0,10):
		while(ans[i] != 0):
			ans_s = ans_s + str(i)
			ans[i] -= 1
	text_file.write('Case #' + str(k) + ': ' + ans_s + '\n')
