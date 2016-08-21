import itertools

tries = int(raw_input())
a = range(10)

for case in range(tries):
	line = raw_input()
	qs = line.count("?")
	minscore = ""
	minval = 0
	for it in itertools.product(a, repeat=qs):
		nums = line.replace("?", "%s")
		nums = nums % it
		numsn = nums.split(" ")
		lnum = int(numsn[0])
		rnum = int(numsn[1])
		#print lnum, rnum, abs(rnum - lnum)
		if abs(rnum - lnum) < minval or minscore == "":
			minscore = nums
			minval = abs(rnum - lnum)

		if minval == 0:
			break

	print("Case #"+str(case+1)+": "+minscore)
			
