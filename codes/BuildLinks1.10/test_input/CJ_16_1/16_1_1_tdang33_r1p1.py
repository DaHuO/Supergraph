T = int(raw_input())

for case in range(1, T+1):
	#= map(int, raw_input().split(" "))
	#K,C,S = map(int, raw_input().split(' '))
	#print "Case #{}: {}".format(case, ' '.join(str(x) for x in X))
	
	S = raw_input()
	y = ""
	y += S[0]
	temp_ch = S[0]
	for i in range(1, len(S)):
		if (S[i] >= temp_ch):
			y = S[i] + y
			temp_ch = S[i]
		else:
			y = y + S[i]
	print "Case #{}: {}".format(case, y)