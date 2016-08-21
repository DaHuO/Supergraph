l = input()
for z in range(0, l):
	S = map(ord,list(raw_input()))
	memo = []
	for m in S:
		if memo == []:
			memo.append(m)
		else:
			if m < memo[0]:
				memo.append(m)
			else:
				memo[:0] = [m]
	print "Case #{}: {}".format(z + 1, "".join(map(chr, memo)))
		
			
		
	