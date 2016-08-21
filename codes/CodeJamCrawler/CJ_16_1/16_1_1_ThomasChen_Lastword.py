
def foo(ss):
	resStr = [ss[0]]
	temp = ss[0]
	for idx in range(1,len(ss)):
		if ss[idx] < temp:
			resStr.append(ss[idx])
		else:
			resStr.insert(0, ss[idx])
			temp = ss[idx]
	return ''.join(resStr)

with open("A-large.in") as readfile:
	with open ("output.txt", "w") as writefile:
		N  = int(readfile.readline())
		for x in range(N):
			ss = readfile.readline().strip()
			resStr = foo(ss)
			writefile.write("Case #" + str(x+1) + ": " + resStr + "\n")