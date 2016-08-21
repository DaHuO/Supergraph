for idx in range(int(raw_input())):
	ipStr = list(raw_input().strip())
	opStr = []
	ch = ipStr[0]
	opStr.append(ch)
	for jdx in range(1, len(ipStr)):
		if ipStr[jdx] >= ch:
			opStr[:0] = ipStr[jdx]
			ch = ipStr[jdx]
		else:
			opStr.append(ipStr[jdx])
		##print "ch: ", ch
	##ipStr.sort()
	##ipStr.reverse()
	##print "Case #" + str(idx) + ": " + " ".join(ipStr.reverse())
	print "Case #" + str(idx+1) + ": " + "".join(opStr)