def checkArray(a):
	s = sum(a)
	if s == 10:
		return True
	else:
		return False
def markNumber(a, s):
	for ch in s:
		n =  ord(ch) - 48
		a[n] = 1
		#print(n)
def lastNo(N):
	steps = 1
	a = [0] * 10
	markNumber(a, str(N))
	no = N
	while not checkArray(a):
		steps += 1
		no = (steps) * N
		markNumber(a, str(no))
	#print("%d => %d"%(N, no))
	return no
lastNo(1234567890)
out = open("output.txt", "w")
with open("input.in", "r") as f:
	s = f.read().split("\n")
	s = s[:len(s)-1]
	t = int(s[0])
	for i in range(1, len(s)):
		number = int(s[i])
		if number == 0:
			st = ("Case #%d: %s" % (i, "INSOMNIA"))
		else:
			st = ("Case #%d: %d" % (i,lastNo(number)))
		print(st)
		out.write(st+"\n")