def flipPancakes(s):
	k = s[len(s)-1]
	if k == '+':
		flips = 0
	else:
		flips = 1
	
	for i in range(len(s)-1, -1, -1):
		if s[i] != k:
			flips += 1
			k = s[i]
	return flips

T = int(raw_input().strip())
for i in range(0,T):
	S = raw_input().strip()
	print 'Case #' + str(i+1) + ':', flipPancakes(S)