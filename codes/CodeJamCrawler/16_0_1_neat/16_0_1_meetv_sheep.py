def last(N):
	p = 1
	a = [0] * 10
	mark(a, str(N))
	n = N
	while not check(a):
		p += 1
		n = (p) * N
		mark(a, str(n))
	return n

def check(a):
	s = sum(a)
	if s == 10:
		return True
	else:
		return False

def mark(a, s):
	for ch in s:
		n =  ord(ch) - 48
		a[n] = 1
		
#last(1234567890)

out = open("output.txt", "w")

with open("A-large.in", "r") as f:
	s = f.read().split("\n")
	s = s[:len(s)-1]
	t = int(s[0])
	for i in range(1, len(s)):
		number = int(s[i])
		if number == 0:
			st = ("Case #%d: %s" % (i, "INSOMNIA"))
		else:
			st = ("Case #%d: %d" % (i,last(number)))
		print(st)
		out.write(st+"\n")