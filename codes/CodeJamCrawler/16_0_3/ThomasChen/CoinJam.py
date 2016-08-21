def foo(N, J):
	resList = set()
	count = 0
	resStr = ""
	if N < 10:
		return resStr
	while count < J:
		# 4 * 2
		for x5 in xrange(1, N - 4):
			x1 = N - x5 - 1
			for x2 in xrange(x1-1,2,-1):
				for x3 in xrange(x2-1 , 1, -1):
					for x4 in xrange(x3 - 1, 0, -1):
						tset = set([0,x1,x2,x3,x4,x5,x5+x1,x5+x2,x5+x3,x5+x4])
						if len(tset) != 10:
							continue
						li = [0 for idx in range(N)]
						li[0]= li[x1]=li[x2]=li[x3]=li[x4]=li[x5]=li[x5+x1]=li[x5+x2]=li[x5+x3]=li[x5+x4] = 1
						binRes = "".join(str(r) for r in li)
						if binRes in resList:
							continue
						else:
							resList.add(binRes)

						# div
						divisions = [(1 + ix**x5) for ix in range(2, 11)]
						divRes = "".join((" "+ str(r)) for r in divisions)
						resStr = resStr + binRes + divRes + "\n"
						count += 1
						if count == J:
							break
					if count == J:
						break
				if count == J:
					break
			if count == J:
				break
		if count == J:
			break

	return resStr

with open("C-large.in") as readfile:
	with open ("output.txt", "w") as writefile:
		T = int(readfile.readline())
		args = [int(elm) for elm in readfile.readline().split(" ")]
		N, J = args[0], args[1]
		for x in range(T):
			resStr = foo(N, J)
			writefile.write("Case #" + str(x+1) + ":\n" + resStr)