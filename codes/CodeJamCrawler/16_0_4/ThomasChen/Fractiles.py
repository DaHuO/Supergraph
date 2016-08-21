
def foo(K, C, S):
	resStr = ""
	for x in xrange(K):
		tempSum = 0
		for y in xrange(1, C):
			tempSum += (K**y)
		resNum = tempSum * x + x + 1
		resStr += str(resNum) + " "
	return resStr

with open("D-small-attempt0.in") as readfile:
	with open ("output.txt", "w") as writefile:
		N  = int(readfile.readline())
		for x in range(N):
			arr = [int(elm.strip()) for elm in readfile.readline().split(" ")]
			K = arr[0]
			C = arr[1]
			S = arr[2]
			resStr = foo(K, C, S)
			writefile.write("Case #" + str(x+1) + ": " + resStr + "\n")